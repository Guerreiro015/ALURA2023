
let nomes = ["João", "Ana", "Caio", "Lara", "Marjorie", "Leo"];

//Reoveremos a Ana, Caio e Lara da lista

nomes.splice(1, 3) // A partir do indice 1 remove 3 itens da lista
console.log(nomes)

let nome = ["João", "Ana", "Caio", "Lara", "Marjorie", "Leo"];
nome.splice(2, 1, 'Rodrigo') // A partir do indice 2 remove 1 itens da lista e adiciona o Rodrigo

console.log(nome)
///////

mor = ["João", "Ana", "Caio", "Lara", "Marjorie", "Leo"];
mor.splice(3,2, 'antonio neto') // Remove dois itens a partir do indice 3
mor.push('Francisca')// acrescenta Francisca no fim da lista
mor.shift() // Remove o primeiro item da lista
console.log(mor)
