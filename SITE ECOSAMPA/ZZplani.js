
const XLSX = require("xlsx");       

const file = 'relatorio.xlsx';
const workbook = XLSX.readFile(file);
const sheetName = workbook.SheetNames[0];
const worksheet = workbook.Sheets[sheetName];
const data = XLSX.utils.sheet_to_json(worksheet, { header: 1 });

console.log(data);


for(i=0;i<data.length;i++){
    if(data[i][4]=='OPERAÇÃO')
    console.log(data[i][4],'--',data[i][9],'--',data[i][10]);
};