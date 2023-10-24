//Vamos filtar os clientes que tem apartamento e não tem complemento
// hasOwnProperty serve para verificar se o objeto tem uma propiedade

const clientes = require("./dadosExercicioJSON.json");

function filtrar(dados) {
    return dados.filter((cliente) => {
        return (
            cliente.endereco.apartamento &&
            !cliente.endereco.hasOwnProperty("complemento")
        );
    });
}

const filtrados = filtrar(clientes);

console.log(filtrados);

let veri;
for(i = 0; i < clientes.length; i++ ){

    veri = clientes[i].endereco.hasOwnProperty("complemento");

    console.log(`\n O cliente ${clientes[i].nome} tem o campo complemento ${veri}`);

}