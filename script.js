
const items=['Iniciar','Specs','Status','Sair'];
let current=0;

const pages={
Iniciar:`<div class="title">INICIAR INFERÊNCIA</div><div class="line"></div><div class="text">Ativa o pipeline de visão computacional embarcada.<br>Câmera, modelos de IA e transmissão em tempo real.</div><div class="box"><div class="row active">● CÂMERA ONLINE</div><div class="row active">● GPU EMBARCADA PRONTA</div><div class="row">○ INFERÊNCIA IA AGUARDANDO</div><div class="row active">● CONEXÃO IOT ATIVO</div></div><button id="btn-iniciar" onclick="toggleCD()">INICIAR INFERÊNCIA</button>`,
Specs:`<div class="title">ESPECIFICAÇÕES</div><div class="line"></div><div class="text">AINDA EM DESENVOLVIMENTO</div>`,
Status:`<div class="title">STATUS</div><div class="line"></div><div class="text">AINDA EM DESENVOLVIMENTO, INFORMAR AS SAÍDAS NO TERMINAL</div>`,
Sair:`<div class="title">SAIR</div><div class="line"></div><div class="text">Tem certeza que deseja sair?</div><div class="box"><div class="row active">● SAIR</div><div class="row">○ CANCELAR</div></div>`
};

function render(){
const menu=document.getElementById('menu');
menu.innerHTML='';
for(let i=0;i<items.length;i++){
 const rel=(i-current+items.length)%items.length;
 if(rel===0) continue;
 const d=document.createElement('div');
 d.className='menu-item';
 d.innerText=items[i];

 const pos={1:[320,120,-14],2:[300,30,-22],3:[320,300,10]}[rel];
 d.style.left=pos[0]+'px';
 d.style.top=pos[1]+'px';
 d.style.transform=`rotate(${pos[2]}deg)`;
 d.style.opacity=1-(Math.abs(pos[2])/30);
 menu.appendChild(d);
}
document.getElementById('selected').innerText=items[current];
document.getElementById('panel').innerHTML=pages[items[current]];
}
render();

let cdAtivo = false;

function toggleCD() {
  const cd = document.querySelector('.cd');
  const btn = document.getElementById('btn-iniciar');
  cdAtivo = !cdAtivo;
  cd.classList.toggle('spinning', cdAtivo);
  btn.textContent = cdAtivo ? 'PARAR INFERÊNCIA' : 'INICIAR INFERÊNCIA';
}

addEventListener('keydown',e=>{
 if(e.key==='ArrowDown'){current=(current+1)%items.length;render();}
 if(e.key==='ArrowUp'){current=(current-1+items.length)%items.length;render();}
});
