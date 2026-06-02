"""
server.py — Zephiro
Serve o index.html e controla o script_inferencia.py via HTTP.

Uso:
    pip install flask
    python server.py

Depois abra no navegador: http://localhost:5000
"""

import sys
import signal
import subprocess
from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_folder='.')

proc = None   # referência ao subprocesso de inferência


# ── Rotas estáticas ────────────────────────────────────────────────

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/assets/<path:filename>')
def assets(filename):
    return send_from_directory('assets', filename)

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)


# ── API de controle ────────────────────────────────────────────────

@app.route('/start', methods=['POST'])
def start():
    global proc
    # Já está rodando
    if proc is not None and proc.poll() is None:
        return jsonify(status='already_running')

    # Inicia o script de inferência
    proc = subprocess.Popen(
        [sys.executable, 'script_inferencia.py'],
        stdin=subprocess.PIPE   # permite enviar Enter pelo stdin se necessário
    )
    print(f'[ZEPHIRO] Inferência iniciada (PID {proc.pid})')
    return jsonify(status='started', pid=proc.pid)


@app.route('/stop', methods=['POST'])
def stop():
    global proc
    if proc is None or proc.poll() is not None:
        return jsonify(status='not_running')

    # Envia SIGINT (equivalente a Ctrl+C / pressionar Q no terminal)
    try:
        proc.send_signal(signal.SIGINT)
        proc.wait(timeout=6)
        print(f'[ZEPHIRO] Inferência encerrada.')
    except subprocess.TimeoutExpired:
        proc.kill()
        print(f'[ZEPHIRO] Inferência forçada a encerrar (timeout).')
    except Exception as e:
        print(f'[ZEPHIRO] Erro ao encerrar: {e}')

    proc = None
    return jsonify(status='stopped')


# ── Limpeza ao fechar o servidor ───────────────────────────────────

def cleanup(signum=None, frame=None):
    global proc
    if proc and proc.poll() is None:
        print('[ZEPHIRO] Encerrando inferência antes de sair...')
        proc.send_signal(signal.SIGINT)
        try:
            proc.wait(timeout=4)
        except Exception:
            proc.kill()
    sys.exit(0)

signal.signal(signal.SIGTERM, cleanup)
signal.signal(signal.SIGINT,  cleanup)


# ── Main ───────────────────────────────────────────────────────────

if __name__ == '__main__':
    print('=' * 50)
    print('  ZEPHIRO — servidor iniciado')
    print('  Acesse: http://localhost:5000')
    print('  Ctrl+C para encerrar')
    print('=' * 50)
    app.run(host='0.0.0.0', port=5000, debug=False)
