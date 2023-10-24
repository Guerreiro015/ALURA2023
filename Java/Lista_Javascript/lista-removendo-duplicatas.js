let meninos = ["Ana", "Marcos", "Mauro", "Mauro","Ana", "Caio vinicius", "Ana"];

let semduplicatas = new Set(meninos)

// foi transformada em um set sem duplicatas
// Vamos trasformar em lista de novo
let novalista = [...semduplicatas]
console.log(semduplicatas)
console.log(novalista)

// Uma forma mais concisa


const nomesAtualizados = [...new Set(meninos)];

console.log(nomesAtualizados);