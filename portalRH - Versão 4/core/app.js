import { UI } from './ui.js';
import { Router } from './router.js';
import { MODULOS } from './modules.js';
import { ExcelService, carregarBaseLocal } from '../services/excel.service.js';
import { ColaboradorService } from '../services/colaborador.service.js';
import { IndexedDBService } from '../services/indexeddb.service.js';

const PERFIS = {
  ADMIN: 'Admin',
  RH: 'RH/DP',
  CONSULTA: 'Consulta'
};

const PERMISSOES = {
  Admin: ['importar-base', 'gerar-documento', 'configuracoes', 'limpar-base', 'limpar-historico', 'usuarios', 'relatorios', 'backup', 'auditoria'],
  'RH/DP': ['importar-base', 'gerar-documento', 'relatorios'],
  Consulta: []
};

const USUARIOS_PADRAO = [
  { id: 'admin', nome: 'Administrador', perfil: 'Admin', pin: '1234', ativo: true },
  { id: 'rh', nome: 'RH / DP', perfil: 'RH/DP', pin: '1234', ativo: true },
  { id: 'consulta', nome: 'Consulta', perfil: 'Consulta', pin: '1234', ativo: true }
];

window.PortalRH = {
  empresa: 'Empresa Tonhão Ltda',
  usuario: null,
  colaborador: null,
  solicitacoes: 0,
  historico: [],
  atualizarHistoricoColaborador: null,
  temPermissao
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


function obterAuditoria() {
  return JSON.parse(localStorage.getItem('portal-auditoria') || '[]');
}

function registrarAuditoria(acao, detalhes = '') {
  const logs = obterAuditoria();
  const usuario = PortalRH.usuario || { nome: 'Sistema', perfil: 'Sistema' };
  logs.unshift({
    data: new Date().toLocaleDateString('pt-BR'),
    hora: new Date().toLocaleTimeString('pt-BR'),
    dataISO: new Date().toISOString(),
    usuario: usuario.nome,
    perfil: usuario.perfil,
    acao,
    detalhes
  });
  localStorage.setItem('portal-auditoria', JSON.stringify(logs.slice(0, 1000)));
  atualizarAuditoriaTela();
}

function atualizarAuditoriaTela() {
  const tabela = document.getElementById('tabelaAuditoria');
  if (!tabela) return;

  const filtroAcao = document.getElementById('filtroAcaoAuditoria')?.value || '';
  const filtroUsuario = document.getElementById('filtroUsuarioAuditoria')?.value || '';
  const logs = obterAuditoria();

  const usuarios = [...new Set(logs.map(l => l.usuario || 'Sistema'))].sort();
  const acoes = [...new Set(logs.map(l => l.acao || 'Ação'))].sort();

  const selUsuario = document.getElementById('filtroUsuarioAuditoria');
  const selAcao = document.getElementById('filtroAcaoAuditoria');

  if (selUsuario && !selUsuario.dataset.loaded) {
    selUsuario.innerHTML = '<option value="">Todos os usuários</option>' + usuarios.map(u => `<option>${UI.safe(u)}</option>`).join('');
    selUsuario.dataset.loaded = '1';
  }
  if (selAcao && !selAcao.dataset.loaded) {
    selAcao.innerHTML = '<option value="">Todas as ações</option>' + acoes.map(a => `<option>${UI.safe(a)}</option>`).join('');
    selAcao.dataset.loaded = '1';
  }

  const filtrados = logs.filter(l => {
    const okUsuario = !filtroUsuario || l.usuario === filtroUsuario;
    const okAcao = !filtroAcao || l.acao === filtroAcao;
    return okUsuario && okAcao;
  });

  const total = document.getElementById('totalAuditoria');
  if (total) total.textContent = filtrados.length;

  tabela.innerHTML = filtrados.slice(0, 150).map(l => `
    <tr>
      <td>${UI.safe(l.data)} ${UI.safe(l.hora)}</td>
      <td>${UI.safe(l.usuario)}</td>
      <td>${UI.safe(l.perfil)}</td>
      <td>${UI.safe(l.acao)}</td>
      <td>${UI.safe(l.detalhes || '---')}</td>
    </tr>
  `).join('') || '<tr><td colspan="5">Nenhum registro de auditoria encontrado.</td></tr>';
}

function exportarAuditoriaCSV() {
  if (!temPermissao('auditoria')) return UI.toast('Acesso negado', 'Somente Admin pode exportar auditoria.');
  const logs = obterAuditoria();
  if (!logs.length) return UI.toast('Atenção', 'Não há registros de auditoria para exportar.');
  const linhas = [['Data', 'Hora', 'Usuário', 'Perfil', 'Ação', 'Detalhes']];
  logs.forEach(l => linhas.push([l.data, l.hora, l.usuario, l.perfil, l.acao, l.detalhes]));
  const csv = linhas.map(linha => linha.map(valor => `"${String(valor || '').replaceAll('"', '""')}"`).join(';')).join('\n');
  const blob = new Blob(['\ufeff' + csv], { type: 'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `auditoria_portal_rh_${new Date().toISOString().slice(0, 10)}.csv`;
  a.click();
  URL.revokeObjectURL(url);
  UI.toast('Auditoria exportada', 'Arquivo CSV gerado com sucesso.');
}

function limparAuditoria() {
  if (!temPermissao('auditoria')) return UI.toast('Acesso negado', 'Somente Admin pode limpar auditoria.');
  localStorage.removeItem('portal-auditoria');
  registrarAuditoria('Auditoria limpa', 'Registros anteriores foram removidos deste navegador.');
  UI.toast('Auditoria limpa', 'Os registros de auditoria foram reiniciados.');
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

function calcularRelatorios(historico) {
  const hoje = new Date().toISOString().slice(0, 10);
  const mesAtual = hoje.slice(0, 7);
  const totalHoje = historico.filter(h => h.dataISO === hoje).length;
  const totalMes = historico.filter(h => String(h.dataISO || '').slice(0, 7) === mesAtual).length;
  const colaboradoresUnicos = new Set(historico.map(h => String(h.matricula))).size;
  const porModulo = {};
  const porUsuario = {};

  historico.forEach(h => {
    porModulo[h.modulo] = (porModulo[h.modulo] || 0) + 1;
    porUsuario[h.usuario || 'DP/RH'] = (porUsuario[h.usuario || 'DP/RH'] || 0) + 1;
  });

  return { totalHoje, totalMes, colaboradoresUnicos, porModulo, porUsuario };
}

function atualizarRelatoriosTela() {
  const tela = document.getElementById('reportsView');
  if (!tela) return;

  const historico = obterHistorico();
  const filtroModulo = document.getElementById('filtroModuloRelatorio')?.value || '';
  const filtroUsuario = document.getElementById('filtroUsuarioRelatorio')?.value || '';

  const filtrado = historico.filter(h => {
    const okModulo = !filtroModulo || h.modulo === filtroModulo;
    const okUsuario = !filtroUsuario || (h.usuario || 'DP/RH') === filtroUsuario;
    return okModulo && okUsuario;
  });

  const dados = calcularRelatorios(filtrado);
  document.getElementById('relTotalHoje').textContent = dados.totalHoje;
  document.getElementById('relTotalMes').textContent = dados.totalMes;
  document.getElementById('relTotalGeral').textContent = filtrado.length;
  document.getElementById('relColaboradores').textContent = dados.colaboradoresUnicos;

  const modulos = [...new Set(historico.map(h => h.modulo))].sort();
  const usuarios = [...new Set(historico.map(h => h.usuario || 'DP/RH'))].sort();

  const selModulo = document.getElementById('filtroModuloRelatorio');
  const selUsuario = document.getElementById('filtroUsuarioRelatorio');

  if (selModulo && !selModulo.dataset.loaded) {
    selModulo.innerHTML = '<option value="">Todos os módulos</option>' + modulos.map(m => `<option>${UI.safe(m)}</option>`).join('');
    selModulo.dataset.loaded = '1';
  }

  if (selUsuario && !selUsuario.dataset.loaded) {
    selUsuario.innerHTML = '<option value="">Todos os usuários</option>' + usuarios.map(u => `<option>${UI.safe(u)}</option>`).join('');
    selUsuario.dataset.loaded = '1';
  }

  const rankingModulo = document.getElementById('rankingModulo');
  rankingModulo.innerHTML = Object.entries(dados.porModulo)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10)
    .map(([nome, total]) => `<div class="rank-item"><span>${UI.safe(nome)}</span><strong>${total}</strong></div>`)
    .join('') || '<div class="empty-history"><i class="fa-solid fa-chart-simple"></i><span>Nenhum dado para exibir.</span></div>';

  const rankingUsuario = document.getElementById('rankingUsuario');
  rankingUsuario.innerHTML = Object.entries(dados.porUsuario)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10)
    .map(([nome, total]) => `<div class="rank-item"><span>${UI.safe(nome)}</span><strong>${total}</strong></div>`)
    .join('') || '<div class="empty-history"><i class="fa-solid fa-user-check"></i><span>Nenhum dado para exibir.</span></div>';

  const tabela = document.getElementById('tabelaRelatorio');
  tabela.innerHTML = filtrado.slice(0, 80).map(h => `
    <tr>
      <td>${UI.safe(h.protocolo)}</td>
      <td>${UI.safe(h.data)} ${UI.safe(h.hora)}</td>
      <td>${UI.safe(h.modulo)}</td>
      <td>${UI.safe(h.colaborador)}</td>
      <td>${UI.safe(h.matricula)}</td>
      <td>${UI.safe(h.usuario || 'DP/RH')}</td>
    </tr>
  `).join('') || '<tr><td colspan="6">Nenhuma solicitação encontrada.</td></tr>';
}

function exportarRelatorioCSV() {
  const historico = obterHistorico();
  if (!historico.length) return UI.toast('Atenção', 'Não há solicitações para exportar.');

  const linhas = [
    ['Protocolo', 'Data', 'Hora', 'Módulo', 'Colaborador', 'Matrícula', 'CPF', 'Usuário']
  ];

  historico.forEach(h => linhas.push([
    h.protocolo, h.data, h.hora, h.modulo, h.colaborador, h.matricula, h.cpf, h.usuario || 'DP/RH'
  ]));

  const csv = linhas.map(linha => linha.map(valor => `"${String(valor || '').replaceAll('"', '""')}"`).join(';')).join('\n');
  const blob = new Blob(['\ufeff' + csv], { type: 'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `relatorio_portal_rh_${new Date().toISOString().slice(0, 10)}.csv`;
  a.click();
  URL.revokeObjectURL(url);
  UI.toast('Relatório exportado', 'Arquivo CSV gerado com sucesso.');
}


async function exportarBackupGeral() {
  if (!temPermissao('backup')) return UI.toast('Acesso negado', 'Somente Admin pode exportar backup.');

  const backup = {
    sistema: 'Portal RH',
    empresa: PortalRH.empresa,
    versao: '4.4',
    geradoEm: new Date().toISOString(),
    usuarios: obterUsuarios(),
    historico: obterHistorico(),
    auditoria: obterAuditoria(),
    baseInfo: JSON.parse(localStorage.getItem('portal-base-info') || 'null'),
    colaboradores: await IndexedDBService.listarColaboradores()
  };

  const blob = new Blob([JSON.stringify(backup, null, 2)], { type: 'application/json;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `backup_portal_rh_${new Date().toISOString().slice(0, 10)}.json`;
  a.click();
  URL.revokeObjectURL(url);
  registrarAuditoria('Backup exportado', 'Backup geral exportado em JSON.');
  UI.toast('Backup exportado', 'Arquivo JSON gerado com sucesso.');
}

async function importarBackupGeral(file) {
  if (!temPermissao('backup')) return UI.toast('Acesso negado', 'Somente Admin pode restaurar backup.');

  try {
    const texto = await file.text();
    const backup = JSON.parse(texto);

    if (!backup || backup.sistema !== 'Portal RH') {
      UI.toast('Backup inválido', 'O arquivo selecionado não parece ser um backup do Portal RH.');
      return;
    }

    if (Array.isArray(backup.usuarios)) {
      localStorage.setItem('portal-usuarios', JSON.stringify(backup.usuarios));
      preencherSelectUsuarios();
    }

    if (Array.isArray(backup.historico)) {
      localStorage.setItem('portal-historico', JSON.stringify(backup.historico));
    }

    if (Array.isArray(backup.auditoria)) {
      localStorage.setItem('portal-auditoria', JSON.stringify(backup.auditoria));
    }

    if (backup.baseInfo) {
      localStorage.setItem('portal-base-info', JSON.stringify(backup.baseInfo));
    }

    if (Array.isArray(backup.colaboradores)) {
      await IndexedDBService.salvarColaboradores(backup.colaboradores);
      ExcelService.colaboradores = backup.colaboradores;
      document.getElementById('statusBase').textContent = backup.colaboradores.length ? 'Carregada' : 'Não carregada';
      document.getElementById('totalFuncionarios').textContent = backup.colaboradores.length;
    }

    atualizarInfoBaseLocal();
    atualizarHistoricoTela();
    atualizarHistoricoColaborador();
    atualizarRelatoriosTela();
    atualizarAuditoriaTela();
    atualizarUsuarioTela();
    registrarAuditoria('Backup restaurado', 'Backup importado com sucesso.');
    UI.toast('Backup restaurado', 'Dados restaurados com sucesso neste navegador.');
  } catch (erro) {
    console.error('Erro ao restaurar backup:', erro);
    UI.toast('Erro', 'Não foi possível restaurar o backup selecionado.');
  }
}

function salvarHistorico(item) {
  const historico = obterHistorico();
  historico.unshift(item);
  localStorage.setItem('portal-historico', JSON.stringify(historico.slice(0, 300)));
  atualizarHistoricoTela();
  atualizarHistoricoColaborador();
  atualizarRelatoriosTela();
}

function montarMenus() {
  document.getElementById('menuLateral').innerHTML = `
    <button class="menu-item" id="menuDashboard">
      <i class="fa-solid fa-house"></i><span>Dashboard</span>
    </button>
    <button class="menu-item" id="menuHistorico">
      <i class="fa-solid fa-clock-rotate-left"></i><span>Últimas Solicitações</span>
    </button>
    <button class="menu-item report-link" id="menuRelatorios">
      <i class="fa-solid fa-chart-column"></i><span>Relatórios</span>
    </button>
    <button class="menu-item admin-link" id="menuAuditoria">
      <i class="fa-solid fa-shield-halved"></i><span>Auditoria</span>
    </button>
    <button class="menu-item admin-link" id="menuConfig">
      <i class="fa-solid fa-gear"></i><span>Configurações</span>
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
  if (!temPermissao('gerar-documento')) {
    UI.toast('Acesso negado', 'Seu perfil não tem permissão para gerar documentos.');
    return;
  }

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
    usuario: PortalRH.usuario?.nome || 'DP/RH'
  });

  registrarAuditoria('Documento gerado', `${m.titulo} • ${protocolo} • ${c.nome} (${c.matricula})`);
  UI.toast('Documento gerado', `${m.titulo} gerado com protocolo ${protocolo}.`);
}

function obterUsuarios() {
  let usuarios = JSON.parse(localStorage.getItem('portal-usuarios') || 'null');
  if (!usuarios || !Array.isArray(usuarios) || !usuarios.length) {
    usuarios = USUARIOS_PADRAO;
    localStorage.setItem('portal-usuarios', JSON.stringify(usuarios));
  }
  return usuarios;
}

function salvarUsuarios(usuarios) {
  localStorage.setItem('portal-usuarios', JSON.stringify(usuarios));
  preencherSelectUsuarios();
}

function preencherSelectUsuarios() {
  const select = document.getElementById('loginUsuario');
  if (!select) return;
  const usuarios = obterUsuarios().filter(u => u.ativo !== false);
  select.innerHTML = usuarios.map(u => `<option value="${UI.safe(u.id)}">${UI.safe(u.nome)} • ${UI.safe(u.perfil)}</option>`).join('');
}

function obterUsuarioSalvo() {
  return JSON.parse(localStorage.getItem('portal-sessao') || 'null');
}

function temPermissao(permissao) {
  const perfil = PortalRH.usuario?.perfil;
  return Boolean(perfil && PERMISSOES[perfil]?.includes(permissao));
}

function aplicarPermissoes() {
  const admin = temPermissao('configuracoes');
  document.querySelectorAll('.admin-only,.admin-link').forEach(el => el.classList.toggle('d-none', !admin));
  document.querySelectorAll('.report-link').forEach(el => el.classList.toggle('d-none', !temPermissao('relatorios')));
  document.getElementById('btnImportar')?.classList.toggle('d-none', !temPermissao('importar-base'));
}

function atualizarUsuarioTela() {
  const usuario = PortalRH.usuario;
  const chip = document.getElementById('usuarioLogado');
  if (chip && usuario) chip.innerHTML = `<i class="fa-solid fa-user"></i> ${UI.safe(usuario.nome)} • ${UI.safe(usuario.perfil)}`;

  const info = document.getElementById('infoUsuarioAtual');
  if (info && usuario) info.textContent = `${usuario.nome} - Perfil: ${usuario.perfil}`;
  aplicarPermissoes();
}

function abrirLogin(forcar = false) {
  preencherSelectUsuarios();
  PortalRH.usuario = obterUsuarioSalvo();
  if (PortalRH.usuario && !forcar) {
    atualizarUsuarioTela();
    document.getElementById('loginOverlay')?.classList.remove('show');
    return;
  }
  document.getElementById('loginPin').value = '';
  document.getElementById('loginOverlay')?.classList.add('show');
}

function entrarSistema() {
  const usuarioId = document.getElementById('loginUsuario').value;
  const pin = document.getElementById('loginPin').value.trim();
  const usuario = obterUsuarios().find(u => u.id === usuarioId && u.ativo !== false);

  if (!usuario) {
    UI.toast('Atenção', 'Usuário não encontrado.');
    return;
  }
  if (pin !== String(usuario.pin)) {
    UI.toast('Atenção', 'PIN inválido.');
    return;
  }

  PortalRH.usuario = { id: usuario.id, nome: usuario.nome, perfil: usuario.perfil, entrada: new Date().toISOString() };
  localStorage.setItem('portal-sessao', JSON.stringify(PortalRH.usuario));
  atualizarUsuarioTela();
  document.getElementById('loginOverlay')?.classList.remove('show');
  registrarAuditoria('Login', `Acesso liberado para ${usuario.nome}.`);
  UI.toast('Bem-vindo', `Acesso liberado para ${usuario.nome}.`);
}

function atualizarInfoBaseLocal() {
  const info = document.getElementById('infoBaseLocal');
  if (!info) return;
  const base = JSON.parse(localStorage.getItem('portal-base-info') || 'null');
  if (!base) {
    info.textContent = 'Nenhuma base local carregada.';
    return;
  }
  info.textContent = `Última importação: ${base.data} • ${base.total} colaboradores.`;
}

function abrirModal(titulo, subtitulo, html) {
  document.getElementById('modalTitulo').textContent = titulo;
  document.getElementById('modalSubtitulo').textContent = subtitulo;
  document.getElementById('modalConteudo').innerHTML = html;
  document.getElementById('modalOverlay').classList.add('show');
}

function fecharModal() {
  document.getElementById('modalOverlay').classList.remove('show');
}

function abrirAlterarPin() {
  const u = PortalRH.usuario;
  if (!u) return;
  abrirModal('Alterar PIN', `Usuário: ${u.nome}`, `
    <div class="modal-form">
      <label>PIN atual</label>
      <input id="pinAtual" type="password">
      <label>Novo PIN</label>
      <input id="pinNovo" type="password">
      <label>Confirmar novo PIN</label>
      <input id="pinConfirmar" type="password">
      <button class="btn btn-primary w-100 mt-3" id="btnSalvarMeuPin"><i class="fa-solid fa-key"></i> Salvar novo PIN</button>
    </div>
  `);
}

function salvarMeuPin() {
  const atual = document.getElementById('pinAtual').value.trim();
  const novo = document.getElementById('pinNovo').value.trim();
  const confirmar = document.getElementById('pinConfirmar').value.trim();
  const usuarios = obterUsuarios();
  const idx = usuarios.findIndex(x => x.id === PortalRH.usuario.id);
  if (idx < 0) return;
  if (String(usuarios[idx].pin) !== atual) return UI.toast('Atenção', 'PIN atual inválido.');
  if (novo.length < 4) return UI.toast('Atenção', 'O novo PIN precisa ter pelo menos 4 caracteres.');
  if (novo !== confirmar) return UI.toast('Atenção', 'A confirmação não confere.');
  usuarios[idx].pin = novo;
  salvarUsuarios(usuarios);
  fecharModal();
  registrarAuditoria('PIN alterado', `Usuário ${PortalRH.usuario.nome} alterou o próprio PIN.`);
  UI.toast('PIN alterado', 'Seu PIN foi atualizado com sucesso.');
}

function abrirGerenciarUsuarios() {
  if (!temPermissao('usuarios')) {
    UI.toast('Acesso negado', 'Somente Admin pode gerenciar usuários.');
    return;
  }
  const linhas = obterUsuarios().map(u => `
    <tr>
      <td><input class="user-nome" data-id="${UI.safe(u.id)}" value="${UI.safe(u.nome)}"></td>
      <td>
        <select class="user-perfil" data-id="${UI.safe(u.id)}">
          ${Object.values(PERFIS).map(p => `<option ${p === u.perfil ? 'selected' : ''}>${p}</option>`).join('')}
        </select>
      </td>
      <td><input class="user-pin" data-id="${UI.safe(u.id)}" value="${UI.safe(u.pin)}"></td>
      <td><input class="user-ativo" data-id="${UI.safe(u.id)}" type="checkbox" ${u.ativo !== false ? 'checked' : ''}></td>
    </tr>
  `).join('');
  abrirModal('Usuários e permissões', 'Controle local de acesso ao Portal RH', `
    <div class="users-toolbar">
      <button class="btn btn-outline-primary" id="btnAdicionarUsuario"><i class="fa-solid fa-user-plus"></i> Adicionar usuário</button>
    </div>
    <div class="table-responsive">
      <table class="table-users">
        <thead><tr><th>Nome</th><th>Perfil</th><th>PIN</th><th>Ativo</th></tr></thead>
        <tbody>${linhas}</tbody>
      </table>
    </div>
    <button class="btn btn-primary w-100 mt-3" id="btnSalvarUsuarios"><i class="fa-solid fa-floppy-disk"></i> Salvar usuários</button>
    <small class="security-note">Permissões: Admin gerencia tudo; RH/DP importa base e gera documentos; Consulta apenas pesquisa e visualiza.</small>
  `);
}

function adicionarUsuarioNoModal() {
  const tbody = document.querySelector('.table-users tbody');
  const id = `user_${Date.now()}`;
  tbody.insertAdjacentHTML('beforeend', `
    <tr>
      <td><input class="user-nome" data-id="${id}" value="Novo usuário"></td>
      <td><select class="user-perfil" data-id="${id}">${Object.values(PERFIS).map(p => `<option>${p}</option>`).join('')}</select></td>
      <td><input class="user-pin" data-id="${id}" value="1234"></td>
      <td><input class="user-ativo" data-id="${id}" type="checkbox" checked></td>
    </tr>
  `);
}

function salvarUsuariosModal() {
  const ids = [...document.querySelectorAll('.user-nome')].map(el => el.dataset.id);
  const usuarios = ids.map(id => ({
    id,
    nome: document.querySelector(`.user-nome[data-id="${id}"]`).value.trim() || 'Usuário',
    perfil: document.querySelector(`.user-perfil[data-id="${id}"]`).value,
    pin: document.querySelector(`.user-pin[data-id="${id}"]`).value.trim() || '1234',
    ativo: document.querySelector(`.user-ativo[data-id="${id}"]`).checked
  }));
  salvarUsuarios(usuarios);
  fecharModal();
  registrarAuditoria('Usuários salvos', 'Permissões locais foram atualizadas.');
  UI.toast('Usuários salvos', 'Permissões atualizadas com sucesso.');
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

    if (e.target.closest('#menuRelatorios')) {
      if (!temPermissao('relatorios')) return UI.toast('Acesso negado', 'Seu perfil não pode abrir relatórios.');
      atualizarRelatoriosTela();
      Router.relatorios();
    }

    if (e.target.closest('#menuAuditoria')) {
      if (!temPermissao('auditoria')) return UI.toast('Acesso negado', 'Somente Admin pode abrir a auditoria.');
      atualizarAuditoriaTela();
      Router.auditoria();
    }

    if (e.target.closest('#menuConfig')) {
      if (!temPermissao('configuracoes')) return UI.toast('Acesso negado', 'Somente Admin pode abrir as configurações.');
      atualizarInfoBaseLocal();
      atualizarUsuarioTela();
      Router.configuracoes();
    }

    const gerar = e.target.closest('#btnGerarDocumento');
    if (gerar) gerarDocumento(gerar.dataset.id);

    if (e.target.closest('#btnCancelarModulo')) Router.dashboard();
    if (e.target.closest('#btnFecharModal')) fecharModal();
    if (e.target.closest('#btnAlterarPin')) abrirAlterarPin();
    if (e.target.closest('#btnSalvarMeuPin')) salvarMeuPin();
    if (e.target.closest('#btnGerenciarUsuarios')) abrirGerenciarUsuarios();
    if (e.target.closest('#btnAdicionarUsuario')) adicionarUsuarioNoModal();
    if (e.target.closest('#btnSalvarUsuarios')) salvarUsuariosModal();
    if (e.target.closest('#btnExportarCSV')) exportarRelatorioCSV();
    if (e.target.closest('#btnAtualizarRelatorio')) atualizarRelatoriosTela();
    if (e.target.closest('#btnExportarBackup')) exportarBackupGeral();
    if (e.target.closest('#btnImportarBackup')) document.getElementById('arquivoBackup').click();
    if (e.target.closest('#btnExportarAuditoria')) exportarAuditoriaCSV();
    if (e.target.closest('#btnAtualizarAuditoria')) atualizarAuditoriaTela();
    if (e.target.closest('#btnLimparAuditoria')) limparAuditoria();
  });

  document.addEventListener('change', e => {
    if (e.target.matches('#filtroModuloRelatorio,#filtroUsuarioRelatorio')) atualizarRelatoriosTela();
    if (e.target.matches('#filtroUsuarioAuditoria,#filtroAcaoAuditoria')) atualizarAuditoriaTela();
    if (e.target.matches('#arquivoBackup') && e.target.files.length) importarBackupGeral(e.target.files[0]);
  });
  document.getElementById('btnTema').addEventListener('click', () => UI.darkToggle());
  document.getElementById('btnEntrar').addEventListener('click', entrarSistema);
  document.getElementById('loginPin').addEventListener('keydown', e => { if (e.key === 'Enter') entrarSistema(); });
  document.getElementById('btnSair').addEventListener('click', () => { registrarAuditoria('Logout', `Usuário ${PortalRH.usuario?.nome || 'desconhecido'} saiu do sistema.`); localStorage.removeItem('portal-sessao'); abrirLogin(true); });
  document.getElementById('btnTrocarUsuario')?.addEventListener('click', () => abrirLogin(true));
  document.getElementById('btnLimparHistorico')?.addEventListener('click', () => {
    if (!temPermissao('limpar-historico')) return UI.toast('Acesso negado', 'Somente Admin pode limpar o histórico.');
    localStorage.removeItem('portal-historico'); atualizarHistoricoTela(); atualizarHistoricoColaborador(); registrarAuditoria('Histórico limpo', 'Histórico de solicitações removido.'); UI.toast('Histórico limpo','Registros removidos deste navegador.');
  });
  document.getElementById('btnLimparBase')?.addEventListener('click', async () => {
    if (!temPermissao('limpar-base')) return UI.toast('Acesso negado', 'Somente Admin pode limpar a base local.');
    await IndexedDBService.limparColaboradores(); ExcelService.colaboradores = []; localStorage.removeItem('portal-base-info'); document.getElementById('statusBase').textContent='Não carregada'; document.getElementById('totalFuncionarios').textContent='0'; atualizarInfoBaseLocal(); registrarAuditoria('Base limpa', 'Base local de colaboradores removida.'); UI.toast('Base limpa','A base local foi removida.');
  });
  document.getElementById('btnImportar').addEventListener('click', () => {
    if (!temPermissao('importar-base')) return UI.toast('Acesso negado', 'Seu perfil não pode importar a base.');
    document.getElementById('arquivoExcel').click();
  });
  document.getElementById('arquivoExcel').addEventListener('change', async e => {
    if (!e.target.files.length) return;
    if (!temPermissao('importar-base')) return UI.toast('Acesso negado', 'Seu perfil não pode importar a base.');
    await ExcelService.importar(e.target.files[0]);
    atualizarInfoBaseLocal();
    registrarAuditoria('Base importada', `${e.target.files[0].name} importada com sucesso.`);
    UI.toast('Base carregada', 'Planilha importada com sucesso e salva localmente.');
  });
}

window.addEventListener('DOMContentLoaded', async () => {
  UI.loadTheme();
  obterUsuarios();
  preencherSelectUsuarios();
  montarMenus();
  iniciarRelogio();
  registrarEventos();
  ColaboradorService.iniciar();
  await carregarBaseLocal();
  atualizarInfoBaseLocal();
  atualizarHistoricoTela();
  atualizarHistoricoColaborador();
  atualizarRelatoriosTela();
  atualizarAuditoriaTela();
  abrirLogin();
  UI.hideLoader();
});
