import { MODULOS } from './modules.js';
import { UI } from './ui.js';

export const Router = {
  abrir(id){
    const modulo=MODULOS.find(m=>m.id===id); if(!modulo) return;
    document.getElementById('dashboardView').classList.remove('active');
    document.getElementById('historyView')?.classList.remove('active');
    document.getElementById('moduleView').classList.add('active');
    document.getElementById('btnVoltarDashboard').classList.remove('d-none');
    document.querySelectorAll('.menu-item').forEach(b=>b.classList.toggle('active', b.dataset.module===id));
    UI.setTitle(modulo.titulo, modulo.descricao);
    document.getElementById('workspace').innerHTML=this.renderFormulario(modulo);
  },
  dashboard(){
    document.getElementById('moduleView').classList.remove('active');
    document.getElementById('historyView')?.classList.remove('active');
    document.getElementById('dashboardView').classList.add('active');
    document.getElementById('btnVoltarDashboard').classList.add('d-none');
    document.querySelectorAll('.menu-item').forEach(b=>b.classList.remove('active'));
    UI.setTitle('Dashboard','Central de solicitações do DP/RH');
  },
  historico(){
    document.getElementById('dashboardView').classList.remove('active');
    document.getElementById('moduleView').classList.remove('active');
    document.getElementById('historyView')?.classList.add('active');
    document.getElementById('btnVoltarDashboard').classList.remove('d-none');
    document.querySelectorAll('.menu-item').forEach(b=>b.classList.toggle('active', b.id === 'menuHistorico'));
    UI.setTitle('Últimas Solicitações','Histórico geral de solicitações geradas no Portal RH');
  },
  renderFormulario(m){
    const c=window.PortalRH.colaborador;
    if(!c) return `<div class="alert alert-warning"><strong>Atenção:</strong> pesquise e selecione um colaborador antes de abrir esta solicitação.</div>`;
    const campos=m.campos.map(campo=>this.renderCampo(campo)).join('');
    return `<div class="form-header"><div><h3>${UI.safe(m.titulo)}</h3><p>${UI.safe(m.descricao)}</p></div><span class="badge bg-primary">${UI.safe(m.categoria)}</span></div>
      <div class="form-card"><h4>Dados do colaborador</h4><div class="form-grid">
      ${this.readonly('Nome',c.nome)}${this.readonly('Matrícula',c.matricula)}${this.readonly('Cargo',c.cargo)}${this.readonly('CPF',c.cpf)}${this.readonly('Empresa',c.empresa)}${this.readonly('Data',new Date().toLocaleDateString('pt-BR'))}</div></div>
      <div class="form-card"><h4>Dados da solicitação</h4><div class="form-grid">${campos}</div><div class="form-actions"><button class="btn btn-secondary" id="btnCancelarModulo">Cancelar</button><button class="btn btn-primary" id="btnGerarDocumento" data-id="${m.id}"><i class="fa-solid fa-print"></i> Gerar Documento</button></div></div>`;
  },
  readonly(label,value){ return `<div class="field"><label>${label}</label><input readonly value="${UI.safe(value)}"></div>`; },
  renderCampo(c){
    const req=c.obrigatorio?'data-required="1"':'';
    if(c.tipo==='select') return `<div class="field"><label>${UI.safe(c.label)}</label><select id="campo_${c.id}" ${req}><option value="">Selecione...</option>${(c.opcoes||[]).map(o=>`<option>${UI.safe(o)}</option>`).join('')}</select></div>`;
    if(c.tipo==='textarea') return `<div class="field full"><label>${UI.safe(c.label)}</label><textarea id="campo_${c.id}" rows="4" ${req}></textarea></div>`;
    if(c.tipo==='date') return `<div class="field"><label>${UI.safe(c.label)}</label><input id="campo_${c.id}" type="date" ${req}></div>`;
    return `<div class="field"><label>${UI.safe(c.label)}</label><input id="campo_${c.id}" type="text" ${req}></div>`;
  }
};
