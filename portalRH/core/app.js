import { UI } from './ui.js';
import { Router } from './router.js';
import { MODULOS } from './modules.js';
import { ExcelService } from '../services/excel.service.js';
import { ColaboradorService } from '../services/colaborador.service.js';

window.PortalRH = {
  empresa: 'Empresa Tonhão Ltda',
  colaborador: null,
  solicitacoes: 0,
  historico: [],
  atualizarHistoricoColaborador: null
};

function cardModulo(m) {
  return `
    <article class="module-card cor-${m.cor}" data-module="${m.id}">
      <div class="icon"><i class="fa-solid ${m.icone}"></i></div>
      <h4>${UI.safe(m.titulo)}</h4>
      <p>${UI.safe(m.descricao)}</p>
    </article>
  `;
}

function obterHistorico() {
  return JSON.parse(localStorage.getItem('portal-historico') || '[]');
}

function atualizarHistoricoTela() {
  const box = document.getElementById('historicoGrid');
  if (!box) return;

  const historico = obterHistorico();
  PortalRH.historico = historico;
  PortalRH.solicitacoes = historico.filter(h => h.dataISO === new Date().toISOString().slice(0, 10)).length;

  const totalSolic = document.getElementById('totalSolicitacoes');
  if (totalSolic) totalSolic.textContent = PortalRH.solicitacoes;

  if (!historico.length) {
    box.innerHTML = '<div class="empty-history"><i class="fa-solid fa-clock-rotate-left"></i><span>Nenhuma solicitação gerada ainda.</span></div>';
    return;
  }

  box.innerHTML = historico.slice(0, 8).map(h => `
    <div class="history-item">
      <div>
        <strong>${UI.safe(h.modulo)}</strong>
        <small>${UI.safe(h.protocolo)} • ${UI.safe(h.colaborador)} • Mat. ${UI.safe(h.matricula)}</small>
      </div>
      <span>${UI.safe(h.data)} ${UI.safe(h.hora)}</span>
    </div>
  `).join('');
}

function atualizarHistoricoColaborador() {
  const box = document.getElementById('historicoColaboradorGrid');
  if (!box) return;

  const c = PortalRH.colaborador;
  if (!c) {
    box.innerHTML = '<div class="empty-history"><i class="fa-solid fa-user-clock"></i><span>Selecione um colaborador para visualizar o histórico individual.</span></div>';
    return;
  }

  const historico = obterHistorico().filter(h => String(h.matricula) === String(c.matricula));

  if (!historico.length) {
    box.innerHTML = `<div class="empty-history"><i class="fa-solid fa-folder-open"></i><span>Nenhuma solicitação encontrada para ${UI.safe(c.nome)}.</span></div>`;
    return;
  }

  box.innerHTML = historico.slice(0, 10).map(h => `
    <div class="history-item collaborator-history-item">
      <div>
        <strong>${UI.safe(h.modulo)}</strong>
        <small>${UI.safe(h.protocolo)} • ${UI.safe(h.data)} às ${UI.safe(h.hora)}</small>
      </div>
      <span>${UI.safe(h.usuario || 'DP/RH')}</span>
    </div>
  `).join('');
}

PortalRH.atualizarHistoricoColaborador = atualizarHistoricoColaborador;

function salvarHistorico(item) {
  const historico = obterHistorico();
  historico.unshift(item);
  localStorage.setItem('portal-historico', JSON.stringify(historico.slice(0, 300)));
  atualizarHistoricoTela();
  atualizarHistoricoColaborador();
}

function montarMenus() {
  document.getElementById('menuLateral').innerHTML = `
    <button class="menu-item" id="menuDashboard">
      <i class="fa-solid fa-house"></i><span>Dashboard</span>
    </button>
    <button class="menu-item" id="menuHistorico">
      <i class="fa-solid fa-clock-rotate-left"></i><span>Últimas Solicitações</span>
    </button>
  ` + MODULOS.map(m => `
    <button class="menu-item" data-module="${m.id}">
      <i class="fa-solid ${m.icone}"></i><span>${UI.safe(m.titulo)}</span>
    </button>
  `).join('');

  document.getElementById('modulesGrid').innerHTML = MODULOS.map(cardModulo).join('');
  document.getElementById('favoritosGrid').innerHTML = MODULOS.filter(m => m.favorito).map(cardModulo).join('');
}

function iniciarRelogio() {
  const tick = () => document.getElementById('horaAtual').textContent = new Date().toLocaleTimeString('pt-BR');
  tick();
  setInterval(tick, 1000);
}

function gerarProtocolo() {
  const data = new Date().toISOString().slice(0, 10).replaceAll('-', '');
  const seq = Math.floor(1000 + Math.random() * 9000);
  return `RH-${data}-${seq}`;
}

function criarHTMLDocumento(m, c, protocolo, dados) {
  const dataAtual = new Date().toLocaleDateString('pt-BR');
  const horaAtual = new Date().toLocaleTimeString('pt-BR');
  const linhasExtras = Object.entries(dados).map(([k, v]) => `
    <tr>
      <th>${UI.safe(k)}</th>
      <td>${UI.safe(v)}</td>
    </tr>
  `).join('');

  return `
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>${UI.safe(m.titulo)} - ${UI.safe(protocolo)}</title>
<style>
  *{box-sizing:border-box}
  body{font-family:Arial,Helvetica,sans-serif;color:#111827;margin:0;background:#f3f4f6;padding:24px}
  .page{max-width:850px;margin:auto;background:#fff;padding:42px;border-radius:8px;box-shadow:0 10px 30px rgba(0,0,0,.08)}
  .header{display:flex;align-items:center;justify-content:space-between;border-bottom:4px solid #1e3a8a;padding-bottom:18px;margin-bottom:24px}
  .brand h1{font-size:24px;margin:0;color:#1e3a8a;letter-spacing:.5px}.brand p{margin:5px 0 0;color:#475569;font-size:13px}
  .protocol{border:1px solid #cbd5e1;border-radius:8px;padding:10px 14px;text-align:right;font-size:12px;background:#f8fafc}.protocol strong{display:block;color:#1e3a8a;font-size:16px}
  h2{text-align:center;font-size:20px;margin:26px 0 22px;text-transform:uppercase;color:#111827}
  table{width:100%;border-collapse:collapse;margin-bottom:20px}th{width:34%;text-align:left;background:#eff6ff;color:#1e3a8a}th,td{border:1px solid #cbd5e1;padding:10px 12px;font-size:13px;vertical-align:top}
  .section-title{font-weight:bold;color:#1e3a8a;margin:24px 0 10px;font-size:14px;text-transform:uppercase}.obs{min-height:65px}
  .signatures{display:grid;grid-template-columns:1fr 1fr;gap:40px;margin-top:70px}.signature{text-align:center}.line{border-top:1px solid #111827;margin-bottom:8px}.footer{margin-top:34px;border-top:1px solid #e5e7eb;padding-top:12px;color:#64748b;font-size:11px;display:flex;justify-content:space-between}
  @media print{body{background:#fff;padding:0}.page{box-shadow:none;border-radius:0;max-width:none}.no-print{display:none}}
</style>
</head>
<body>
<div class="page">
  <div class="header">
    <div class="brand"><h1>EMPRESA TONHÃO LTDA</h1><p>Portal RH • Departamento Pessoal</p></div>
    <div class="protocol">Protocolo<strong>${UI.safe(protocolo)}</strong></div>
  </div>

  <h2>${UI.safe(m.titulo)}</h2>

  <div class="section-title">Dados do colaborador</div>
  <table>
    <tr><th>Nome</th><td>${UI.safe(c.nome)}</td></tr>
    <tr><th>Matrícula</th><td>${UI.safe(c.matricula)}</td></tr>
    <tr><th>CPF</th><td>${UI.safe(c.cpf)}</td></tr>
    <tr><th>Cargo</th><td>${UI.safe(c.cargo)}</td></tr>
    <tr><th>Folha / Local</th><td>${UI.safe(c.folha || '---')}</td></tr>
    <tr><th>Empresa</th><td>${UI.safe(c.empresa || 'Empresa Tonhão Ltda')}</td></tr>
  </table>

  <div class="section-title">Dados da solicitação</div>
  <table>
    <tr><th>Data da solicitação</th><td>${dataAtual} às ${horaAtual}</td></tr>
    ${linhasExtras}
  </table>

  <div class="signatures">
    <div class="signature"><div class="line"></div><strong>Assinatura do Colaborador</strong></div>
    <div class="signature"><div class="line"></div><strong>Responsável RH/DP</strong></div>
  </div>

  <div class="footer">
    <span>Documento gerado automaticamente pelo Portal RH.</span>
    <span>${dataAtual} ${horaAtual}</span>
  </div>
</div>
</body>
</html>`;
}

function gerarDocumento(id) {
  const m = MODULOS.find(x => x.id === id);
  const c = PortalRH.colaborador;
  if (!m || !c) return;

  const protocolo = gerarProtocolo();
  const dados = {};

  for (const campo of m.campos) {
    const el = document.getElementById(`campo_${campo.id}`);
    if (!el) continue;

    if (campo.obrigatorio && !el.value.trim()) {
      UI.toast('Atenção', `Preencha: ${campo.label}`);
      el.focus();
      return;
    }

    dados[campo.label] = el.value.trim() || '---';
  }

  const html = criarHTMLDocumento(m, c, protocolo, dados);
  const w = window.open('', '_blank');
  w.document.write(html);
  w.document.close();
  w.focus();
  setTimeout(() => w.print(), 300);

  salvarHistorico({
    protocolo,
    modulo: m.titulo,
    colaborador: c.nome,
    matricula: c.matricula,
    cpf: c.cpf,
    data: new Date().toLocaleDateString('pt-BR'),
    hora: new Date().toLocaleTimeString('pt-BR'),
    dataISO: new Date().toISOString().slice(0, 10),
    usuario: 'DP/RH'
  });

  UI.toast('Documento gerado', `${m.titulo} gerado com protocolo ${protocolo}.`);
}

function registrarEventos() {
  document.addEventListener('click', e => {
    const mod = e.target.closest('[data-module]');
    if (mod) Router.abrir(mod.dataset.module);

    if (e.target.closest('#menuDashboard') || e.target.closest('#btnVoltarDashboard')) Router.dashboard();

    if (e.target.closest('#menuHistorico')) {
      atualizarHistoricoTela();
      Router.historico();
    }

    const gerar = e.target.closest('#btnGerarDocumento');
    if (gerar) gerarDocumento(gerar.dataset.id);

    if (e.target.closest('#btnCancelarModulo')) Router.dashboard();
  });

  document.getElementById('btnTema').addEventListener('click', () => UI.darkToggle());
  document.getElementById('btnImportar').addEventListener('click', () => document.getElementById('arquivoExcel').click());
  document.getElementById('arquivoExcel').addEventListener('change', async e => {
    if (!e.target.files.length) return;
    await ExcelService.importar(e.target.files[0]);
    UI.toast('Base carregada', 'Planilha importada com sucesso.');
  });
}

window.addEventListener('DOMContentLoaded', () => {
  UI.loadTheme();
  montarMenus();
  iniciarRelogio();
  registrarEventos();
  ColaboradorService.iniciar();
  atualizarHistoricoTela();
  atualizarHistoricoColaborador();
  UI.hideLoader();
});
