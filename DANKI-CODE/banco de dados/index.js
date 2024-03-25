
//index.js


// nom = 'Antonio'
// ema = 'antonio@email'
// sen = 'senha1234'
// ida = '36'



function inserir() {    
    nom = document.getElementById('nome')
    ema = document.getElementById('senha')
    sen = document.getElementById('senha')
    ida = document.getElementById('idade')

    inserirCliente(nom, ema, sen, ida)
}

//inserir()

async function inserirCliente(nome, email, senha, idade) {
    const db = require("./db");
    console.log('Começou Inserção!');

    console.log('INSERT INTO usuarios');
    const result = await db.insertCustomer({
        nome: nome,
        email: email,
        senha: senha,
        idade: idade,
        createdAt: '2024-03-23 14:17:38',
        updatedAt: '2024-03-23 14:17:38'
    });
    console.log(result);

    console.log('SELECT * FROM usuarios');
    const clientes = await db.selectCustomers();
    console.log(clientes);
};

//inserirCliente()




async function atualizarCliente() {
    try {
        const db = require("./db");
        const result2 = await db.updateCustomer(11, {
            nome: "Luana",
            email: "luana@luana",
            senha: '1234',
            idade: '35',
            createdAt: '2024-03-23 14:17:38',
            updatedAt: '2024-03-23 14:17:38'
        });
        console.log(result2); // Faça algo com o resultado
    } catch (error) {
        console.error("Erro ao atualizar cliente:", error);
    }
}
// Chame a função para executar a atualização
//atualizarCliente();





async function deletar() {
    const db = require("./db");
    const result3 = await db.deleteCustomer(9);
    // Otro código relacionado aquí

}

//deletar();

//index.js
async function visualizarCliente() {
    const db = require("./db");
    console.log('Começou Visualizar!');
    var clientes = await db.selectCustomers();
    //console.log(clientes); 
    return clientes   
   
};

var visual = visualizarCliente();

console.log(visual)




