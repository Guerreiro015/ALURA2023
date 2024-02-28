
Excel.run(async (context) => {
    const sheet = context.workbook.worksheets.getActiveWorksheet("dados.xlsx");
    const range = sheet.getRange("A1:B2");
    range.values = [["Hello", "World"], ["Excel", "JS"]];
    await context.sync();
});

//     // Carrega a propriedade "name" da planilha
//     ws.load("name");

//     // Sincroniza as alterações com o Excel real
//     await context.sync();

//     // Agora você pode acessar a propriedade "name"
//     console.log("Nome da planilha: " + ws.name);
// });