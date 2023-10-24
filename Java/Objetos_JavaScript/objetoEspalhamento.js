const cliente = {
    nome: "Joao",
    idade: 24,
    email: "joao@firma.com",
    telefone: ["1155555550", "22224444440"],
};

cliente.enderecos = [
    {
        rua: "R. Joseph Climber",
        numero: 1337,
        apartamento: true,
        complemento: "ap 934",
    },
]

// vamos criar um função pra listar todos os telefones

tel = function(tel1,tel2){

    console.log(`Ligando para telefone ${tel1}`)
    console.log(`Ligando para telefone ${tel2}\n`)
    
}

//Chamando a funcçao normal
tel(cliente.telefone[0],cliente.telefone[1])

//Chamando a funcçao com espalhamanto ...

tel(...cliente.telefone)

// Vamos criar uma mascara para postagem no correio 
let correio={
    destinatario: cliente.nome, endereco: cliente.enderecos[0]
}

console.log(correio);


//podemos usar o espalhamento para colocarmos apenas os campos da propiedade endereço

let postagem={
    destinatario: cliente.nome, ...cliente.enderecos[0]
}

console.log(postagem);

// Aqui é onde vamos utilizar o spread operator, adicionando a sintaxe de três pontos (reticências) antes do nome de cada objeto literal, separando-os com uma vírgula:

const ficha = {
    nome: "Aragorn",
    classe: "guerreiro"
   }
   
   const equipo = {
    espada: "Andúril",
    capa: "capa élfica +2"
   }

   let guerreiro = {ficha,equipo};

   console.log(guerreiro);

   //juntando com o spread operator ...

   let guerreiro2 = {...ficha, ...equipo};
   
    console.log(guerreiro2);




