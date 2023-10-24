// Calculando as médias usando o FOR

const notas = [10, 6.5, 8, 7.5];
total = 0;
for (i = 0; i < notas.length; i++) {
    total += notas[i]
}

medias = total / notas.length

console.log(`A soma da notas e igual a ${total}`)
console.log(`O total de notas e igual a ${notas.length}`)
console.log(`A média das notas e igual a ${medias}`)


