import { ExcelService } from './excel.service.js';
import { UI } from '../core/ui.js';

export const ColaboradorService = {
  iniciar(){ document.getElementById('txtPesquisa').addEventListener('input', e=>this.buscar(e.target.value)); },
  buscar(texto){
    const lista=document.getElementById('listaPesquisa'); lista.innerHTML='';
    const resultados=ExcelService.pesquisar(texto);
    resultados.forEach(c=>{
      const item=document.createElement('div'); item.className='result-item';
      item.innerHTML=`<strong>${UI.safe(c.nome)}</strong><br><small>Matrícula: ${UI.safe(c.matricula)} • ${UI.safe(c.cargo)} • ${UI.safe(c.folha)}</small>`;
      item.addEventListener('click',()=>this.selecionar(c)); lista.appendChild(item);
    });
  },
  selecionar(c){
    window.PortalRH.colaborador=c;
    document.getElementById('txtPesquisa').value=c.nome;
    document.getElementById('listaPesquisa').innerHTML='';
    const set=(id,val)=>document.getElementById(id).textContent=val || '---';
    set('nomeColaborador',c.nome); set('matriculaColaborador',c.matricula); set('cpfColaborador',c.cpf); set('cargoColaborador',c.cargo); set('empresaColaborador',c.empresa); set('folhaColaborador',c.folha); set('admissaoColaborador',c.admissao); set('horarioColaborador',c.horario); set('situacaoColaborador',c.situacao);
    const st=document.getElementById('statusColaborador'); st.textContent='Colaborador selecionado'; st.className='pill ok';
    UI.toast('Colaborador selecionado', c.nome);
  }
};
