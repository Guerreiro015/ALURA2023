import { run } from '@microsoft/office-js/excel';

// Função assíncrona para criar uma nova pasta de trabalho
async function criarPastaDeTrabalho() {
    try {
        await run(async (context) => {
            // Obtenha o objeto de pasta de trabalho ativo
            const workbook = context.workbook;

            // Crie uma nova planilha
            const sheet = workbook.worksheets.add('Nova Planilha');

            // Adicione algum conteúdo à planilha (opcional)
            sheet.getRange('A1').values = [['Olá, mundo!']];

            // Salve a pasta de trabalho
            await context.sync();

            console.log('Pasta de trabalho criada com sucesso!');
        });
    } catch (error) {
        console.error('Erro ao criar a pasta de trabalho:', error);
    }
}

// Chame a função para criar a pasta de trabalho
//criarPastaDeTrabalho()