
let nomes = ["João", "Ana", "Caio", "Lara", "Marjorie", "Leo"];

//Removeremos a Ana, Caio e Lara da lista

nomes.splice(1, 3) // Remove o intervalo de 1 a 3 da lista
console.log(nomes)

let nome = ["João", "Ana", "Caio", "Lara", "Marjorie", "Leo"];

nome.splice(1, 3, 'Rodrigo') // Remove o intervalo de 1 a 3 da lista e adiciona o Rodrigo

console.log(nome)