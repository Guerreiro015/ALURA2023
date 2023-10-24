var alunos = ["João", "Juliana", "Ana", "Caio"];
var notas = [10, 8, 7.5, 9];
let media = [alunos,notas] // Um lista com duas listas dentro

// Vamos encontrar os itens usando o indice da lista e indice do item.
console.log(media[0][0])
console.log(media[0][1])
console.log(media[0][2])
console.log(media[0][3])

console.log(media[1][0])
console.log(media[1][1])
console.log(media[1][2])
console.log(media[1][3])

// para sabermos a nota de Ana 
let notaana = `A nota de amiga ${media[0][2]}, é ${media[1][2]}
`
console.log(notaana)

for(i=0;i<alunos.length;i++){

resultado =  `A nota de ${media[0][i]}, é ${media[1][i]}`
console.log(resultado)

}



