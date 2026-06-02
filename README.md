# Zephiro 🎯

Interface de controle embarcada para pipeline de visão computacional com YOLO.  
Desenvolvida para rodar em hardware como **Jetson Orin NX**, com menu em arco, animação de CD e integração direta com câmera e modelo treinado.

---

## 📸 Preview

> Menu em arco de 180° com CD animado, seletor, painel de status e controle de inferência em tempo real.

---

## 🗂️ Estrutura do projeto

```
zephiro/
├── assets/
│   ├── bg-grid.png          # fundo com grade
│   ├── CD.png               # imagem do CD (carrossel)
│   ├── selector.png         # seletor do menu
│   └── audios/              # arquivos .wav para alertas de áudio
│       ├── Pessoa_muito_perto.wav
│       ├── Pessoa_se_aproximando.wav
│       ├── Pessoa_distante.wav
│       ├── Carro_muito_perto.wav
│       ├── Carro_se_aproximando.wav
│       └── Carro_distante.wav
├── index.html               # interface principal (HTML/CSS/JS)
├── server.py                # servidor Flask — ponte entre UI e Python
├── script_inferencia.py     # pipeline de visão computacional (YOLO + câmera)
├── requirements.txt
└── README.md
```

---

## ⚙️ Requisitos

- Python 3.10+
- Câmera conectada (índice `0` por padrão)
- Modelo YOLO treinado (`best.pt`) na raiz do projeto

### Dependências Python

```bash
pip install -r requirements.txt
```

| Pacote | Uso |
|---|---|
| `flask` | Servidor HTTP que serve a UI e controla o subprocesso |
| `opencv-python` | Captura de câmera e exibição de frames |
| `ultralytics` | Inferência YOLO |
| `pygame` | Reprodução dos alertas de áudio |

---

## 🚀 Como rodar

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/zephiro.git
cd zephiro
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Coloque seu modelo treinado na pasta**
```bash
# renomeie ou aponte o caminho em script_inferencia.py
cp /caminho/do/seu/best.pt ./best.pt
```

Em `script_inferencia.py`, confirme que a linha do modelo aponta para o seu arquivo:
```python
model = YOLO("best.pt")
```

**4. Inicie o servidor**
```bash
python server.py
```

**5. Abra no navegador**
```
http://localhost:5000
```

> ⚠️ Use **Ctrl + 0** no navegador para garantir zoom em 100% e layout correto.

---

## 🎮 Como usar a interface

| Ação | Resultado |
|---|---|
| `↑` `↓` ou scroll | Navega entre os itens do menu |
| Clicar em **INICIAR INFERÊNCIA** | Inicia o `script_inferencia.py` e anima o CD |
| Clicar em **PARAR INFERÊNCIA** | Encerra o pipeline (equivale a pressionar `Q` no terminal) |
| Navegar até **Sair** → **CONFIRMAR SAÍDA** | Encerra o pipeline e sinaliza saída |

---

## 🧠 Pipeline de inferência

O `script_inferencia.py` realiza:

- Captura de vídeo em tempo real via OpenCV
- Detecção de objetos com YOLOv8 (modelo customizado)
- Classificação de proximidade: **muito perto / se aproximando / distante**
- Alertas de áudio via arquivos `.wav` (pasta `assets/audios/`)
- Fallback de síntese de voz via PowerShell (Windows) se o áudio não existir

### Classes suportadas

`person`, `car`, `truck`, `motorcycle`, `bicycle`, `bus`, `dog`, `cat`, `chair`, `bottle`, `fire hydrant`

---

## 🔌 API do servidor

O `server.py` expõe três endpoints usados pela interface:

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/` | Serve o `index.html` |
| `POST` | `/start` | Inicia o `script_inferencia.py` |
| `POST` | `/stop` | Encerra o processo via `SIGINT` |

---

## 🛠️ Personalização

### Modelo YOLO
```python
# script_inferencia.py
model = YOLO("best.pt")  # troque pelo caminho do seu modelo
```

### Câmera
```python
cap = cv2.VideoCapture(0)  # troque 0 pelo índice da sua câmera
```

### Confiança mínima
```python
CONF = 0.45  # valor entre 0 e 1
```

### Cooldown entre alertas
```python
COOLDOWN = 4.0  # segundos entre alertas da mesma classe
```

---

## 📦 Tecnologias

- **Frontend:** HTML5 · CSS3 · JavaScript vanilla · Rubik One (Google Fonts)
- **Backend:** Python 3 · Flask
- **Visão computacional:** OpenCV · Ultralytics YOLOv8
- **Áudio:** Pygame

---

## 📄 Licença

MIT — sinta-se livre para usar, modificar e distribuir.
