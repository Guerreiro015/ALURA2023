
const XLSX = require("xlsx");       

const file = 'sindicato.xlsx';
const workbook = XLSX.readFile(file);
const sheetName = workbook.SheetNames[0];
const worksheet = workbook.Sheets[sheetName];
const data = XLSX.utils.sheet_to_json(worksheet, { header: 1 });

// console.log(data);
// console.log(data[5]);

for(i=0;i<data.length;i++){
    console.log('ID: ',data[i][0],'Nome:',data[i][1]);
};
