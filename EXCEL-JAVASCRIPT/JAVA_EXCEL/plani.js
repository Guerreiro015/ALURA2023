const botao = document.querySelector('.button');
botao.addEventListener('click', alerta);

function alerta(){
  alert('OLha ai')
}

function busca() {

  const XLSX = require("xlsx");

  const file = 'sindicato.xlsx';
  const workbook = XLSX.readFile(file);
  const sheetName = workbook.SheetNames[0];
  const worksheet = workbook.Sheets[sheetName];
  const data = XLSX.utils.sheet_to_json(worksheet, { header: 1 });


  //console.log(data);

  for (i = 0; i < data.length; i++) {
    if (data[i][4] == 'OPERAÇÃO')
      console.log(data[i][0], '--', data[i][1], '--', data[i][2], '--', data[i][3], '--', data[i][9], '--', data[i][10]);
  };

  const caminhoArquivo = 'dados.json';
  const dadosJSON = JSON.stringify(data, null, 2);

  const fs = require('fs');

  fs.writeFile(caminhoArquivo, dadosJSON, 'utf-8', (err) => {
    if (err) {
      console.error('Erro ao salvar o arquivo:', err);
    } else {
      console.log('Os dados foram salvos com sucesso!');
    }
  });

}



//busca()