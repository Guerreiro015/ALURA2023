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

// Para transformar as propiedades do objeto em uma lista
// Atentar que Object começa com O maiúsculo

let campos = Object.keys(cliente);

console.log(campos);

campos.push("bairro")

console.log(campos);

for (i = 0; i < campos.length; i++){;

console.log(campos[i])
}

if(campos.includes("endereco")){

  console.log(`\n Este cliente tem o campo ${campos[4]}`)
}
else{
  console.log("\n Este client não tem enderecos")
}
