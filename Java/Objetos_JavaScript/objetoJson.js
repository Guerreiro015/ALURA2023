// Os arquivos .json guardam informações que podemos acessar através usando require entre aspas

let pula = function(){
    console.log("\n. pula linha");
}

pula;

const dados = require("./arquivoJSON.json");


console.log(dados);

console.log(typeof dados);

console.log(`O Primeiro do item é ${dados.nome}`);

// "Stringficação" Transformar o objeto em STRING

const dadoString = JSON.stringify(dados); // comando JSON.stringfy

console.log(dadoString)// dados trasnformadoos em string

console.log(typeof dadoString);

// Tranfomar em objeto novamente
 let dadosDeNovo = JSON.parse(dadoString);// comando JSON.parse

 console.log(dadosDeNovo)// dados trasnformadoos em string

console.log(typeof dadosDeNovo);











