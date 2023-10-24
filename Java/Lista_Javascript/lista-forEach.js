const notas = [10, 6.5, 8, 7.5];
total = 0;
notas.forEach(function(nota,contador){
    total += nota
console.log(contador)
})

medias = total / notas.length

console.log(`A soma da notas e igual a ${total}`)
console.log(`O total de notas e igual a ${notas.length}`)
console.log(`A média das notas e igual a ${medias}`)

//Usando array.functions =>

const nomes = ["Evaldo", "Mari", "Camisa"];

nomes.forEach(function (nome) {
  console.log(nome);
}); // Normal

nomes.forEach((nome) => {
  console.log(nome);
});// Usando o array.function =>



// usando forEach com array =>
let note = [10, 20, 15, 12, 30];
let recebevalor = 0
// lista -    função - array  variavel       função
  note.forEach(somador   =>   recebevalor += somador )

  med = recebevalor/note.length
  console.log(recebevalor)
  console.log(med)

   console.log(`A soma da notas e igual a ${recebevalor}`)
   console.log(`O total de notas e igual a ${note.length}`)
   console.log(`A média das notas e igual a ${med}\n`)

