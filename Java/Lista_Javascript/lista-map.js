//O map é usado para alterar um lista

const notas = [10, 6.5, 8, 7.5, 9.5, 12];
//             usamos   array
let total = notas.map((soma) => {
    // usamos operador ternario ( x > y ? a : b)
    return soma + 1 >= 10 ? 10 : soma + 1

})

console.log(total)

// deixar os nomes todos em maiúsculos

let nomes = ["ana Julia", "Caio vinicius", "BIA silva"];

let maiusculas = nomes.map((nome) => {
    return nome.toUpperCase()
})
console.log(maiusculas)

// a mesma coisa sem o return usando apenas o array =>

let meusnomes = ["ana julia", "Caio vinicius", "BIA SILVa"];
// Transformando tudo em maiuscula
let maiucusla = meusnomes.map((nom) => nom.toUpperCase())
// Transformando o maiuscula em minusculo
let minuscula = maiucusla.map((nom) => nom.toLowerCase())
// adicionando alguma coisa a lista
let nova = maiucusla.map((nom) => " Aluno..: "+nom )


console.log(maiucusla+'\n') // ( \n) serve para pular linha
console.log(minuscula+'\n')
console.log(nova+'\n')







