// podemos criar um objeto com listas

const cliente = {
    nome: "Joao",
    idade: 24,
    email: "joao@firma.com",
    telefone: ["1155555550", "1144444440"],
};

cliente.enderecos = [
    {
        rua: "R. Joseph Climber",
        numero: 1337,
        apartamento: true,
        complemento: "ap 934",
    },
];

cliente.enderecos.push({
    rua: "R. Joseph Ladder",
    numero: 404,
    apartamento: false,
});

cliente.enderecos.push({ rua: "minha miga", numero: 123, bairro: "vizinha" })

const listaApenasApartamentos = cliente.enderecos.filter(
    (endereco) => endereco.apartamento === true
);

console.log(listaApenasApartamentos);
console.log(cliente.enderecos)
console.log(cliente)

for(i=0;i<cliente.enderecos.length;i++){
    console.log(cliente.enderecos[1].rua)
    console.log(cliente.enderecos[0].rua)
}
console.log(cliente.enderecos[0].numero)