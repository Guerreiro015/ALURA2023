//podemos usar operador no .map

let note = [10, 20, 15, 12, 30];

let nota = note.map((non) => non+1 > 15 ? 21 : non+1 )

console.log(nota)
