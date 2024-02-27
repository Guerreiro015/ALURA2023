await Excel.run(async (context) => {
    let sheets = context.workbook.worksheets;
    sheets.load("items/name");
    await context.sync();

    if (sheets.items.length > 1) {
        console.log(`Existem ${sheets.items.length} planilhas na pasta de trabalho:`);
    } else {
        console.log(`Existe uma planilha na pasta de trabalho:`);
    }

    sheets.items.forEach((sheet) => {
        console.log(sheet.name);
    });
});