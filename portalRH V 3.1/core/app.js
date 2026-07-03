import { UI } from './ui.js';
import { Router } from './router.js';
import { MODULOS } from './modules.js';
import { ExcelService } from '../services/excel.service.js';
import { ColaboradorService } from '../services/colaborador.service.js';

window.PortalRH = { empresa:'Empresa Tonhão Ltda', colaborador:null, solicitacoes:0, historico:[] };

function cardModulo(m){ return `<article class="module-card cor-${m.cor}" data-module="${m.id}"><div class="icon"><i class="fa-solid ${m.icone}"></i></div><h4>${m.titulo}</h4><p>${m.descricao}</p></article>`; }

function atualizarHistoricoTela(){
  const box=document.getElementById('historicoGrid');
  if(!box) return;
  const historico = JSON.parse(localStorage.getItem('portal-historico') || '[]');
  PortalRH.historico = historico;
  PortalRH.solicitacoes = historico.filter(h=>h.dataISO===new Date().toISOString().slice(0,10)).length;
  const totalSolic=document.getElementById('totalSolicitacoes');
  if(totalSolic) totalSolic.textContent=PortalRH.solicitacoes;
  if(!historico.length){
    box.innerHTML='<div class="empty-history"><i class="fa-solid fa-clock-rotate-left"></i><span>Nenhuma solicitação gerada ainda.</span></div>';
    return;
  }
  box.innerHTML = historico.slice(0,8).map(h=>`<div class="history-item"><div><strong>${UI.safe(h.modulo)}</strong><small>${UI.safe(h.colaborador)} • Mat. ${UI.safe(h.matricula)}</small></div><span>${UI.safe(h.data)} ${UI.safe(h.hora)}</span></div>`).join('');
}

function salvarHistorico(item){
  const historico = JSON.parse(localStorage.getItem('portal-historico') || '[]');
  historico.unshift(item);
  localStorage.setItem('portal-historico', JSON.stringify(historico.slice(0,100)));
  atualizarHistoricoTela();
}

function montarMenus(){
  document.getElementById('menuLateral').innerHTML = `<button class="menu-item" id="menuDashboard"><i class="fa-solid fa-house"></i><span>Dashboard</span></button>` + MODULOS.map(m=>`<button class="menu-item" data-module="${m.id}"><i class="fa-solid ${m.icone}"></i><span>${m.titulo}</span></button>`).join('');
  document.getElementById('modulesGrid').innerHTML = MODULOS.map(cardModulo).join('');
  document.getElementById('favoritosGrid').innerHTML = MODULOS.filter(m=>m.favorito).map(cardModulo).join('');
}
function iniciarRelogio(){ const tick=()=>document.getElementById('horaAtual').textContent=new Date().toLocaleTimeString('pt-BR'); tick(); setInterval(tick,1000); }
function gerarProtocolo(){ return 'RH-' + new Date().toISOString().slice(0,10).replaceAll('-','') + '-' + Math.floor(1000 + Math.random()*9000); }
function gerarDocumento(id){
  const m=MODULOS.find(x=>x.id===id), c=PortalRH.colaborador; if(!m||!c) return;
  const protocolo=gerarProtocolo();
  const dados={};
  for(const campo of m.campos){ const el=document.getElementById(`campo_${campo.id}`); if(campo.obrigatorio && !el.value.trim()){ UI.toast('Atenção',`Preencha: ${campo.label}`); el.focus(); return; } dados[campo.label]=el.value.trim() || '---'; }
  const extras=Object.entries(dados).map(([k,v])=>`<p><strong>${k}:</strong> ${UI.safe(v)}</p>`).join('');
  const html=`<html><head><title>${m.titulo}</title></head><body style="font-family:Arial;padding:38px"><h2 style="text-align:center">EMPRESA TONHÃO LTDA</h2><h3 style="text-align:center">${UI.safe(m.titulo).toUpperCase()}</h3><p style="text-align:center"><strong>Protocolo:</strong> ${protocolo}</p><hr><p><strong>Nome:</strong> ${UI.safe(c.nome)}</p><p><strong>Matrícula:</strong> ${UI.safe(c.matricula)}</p><p><strong>Cargo:</strong> ${UI.safe(c.cargo)}</p><p><strong>CPF:</strong> ${UI.safe(c.cpf)}</p><p><strong>Empresa:</strong> ${UI.safe(c.empresa)}</p><p><strong>Data:</strong> ${new Date().toLocaleDateString('pt-BR')}</p><hr>${extras}<br><br><p>________________________________________</p><p>Assinatura do Colaborador</p><br><p>________________________________________</p><p>Responsável RH/DP</p></body></html>`;
  const w=window.open('','_blank'); w.document.write(html); w.document.close(); w.focus(); w.print();
  salvarHistorico({protocolo, modulo:m.titulo, colaborador:c.nome, matricula:c.matricula, data:new Date().toLocaleDateString('pt-BR'), hora:new Date().toLocaleTimeString('pt-BR'), dataISO:new Date().toISOString().slice(0,10)});
  UI.toast('Documento gerado', `${m.titulo} enviado para impressão.`);
}
function registrarEventos(){
  document.addEventListener('click',e=>{
    const mod=e.target.closest('[data-module]'); if(mod) Router.abrir(mod.dataset.module);
    if(e.target.closest('#menuDashboard') || e.target.closest('#btnVoltarDashboard')) Router.dashboard();
    const gerar=e.target.closest('#btnGerarDocumento'); if(gerar) gerarDocumento(gerar.dataset.id);
    if(e.target.closest('#btnCancelarModulo')) Router.dashboard();
  });
  document.getElementById('btnTema').addEventListener('click',()=>UI.darkToggle());
  document.getElementById('btnImportar').addEventListener('click',()=>document.getElementById('arquivoExcel').click());
  document.getElementById('arquivoExcel').addEventListener('change',async e=>{ if(!e.target.files.length) return; await ExcelService.importar(e.target.files[0]); UI.toast('Base carregada','Planilha importada com sucesso.'); });
}
window.addEventListener('DOMContentLoaded',()=>{ UI.loadTheme(); montarMenus(); iniciarRelogio(); registrarEventos(); ColaboradorService.iniciar(); atualizarHistoricoTela(); UI.hideLoader(); });
