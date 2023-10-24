let meninos = ["Ana", "Marcos", "Maria", "Mauro","ana Julia", "Caio vinicius", "BIA silva"];
let notas = [7, 4.5, 8, 7.5, 6, 10, 3.9];

let aprovados = meninos.filter((aluno, ind) => notas[ind] >= 7)


const alunos = ["Ana", "Marcos", "Maria", "Mauro","ana Julia", "Caio vinicius", "BIA silva"];
const medias = [7, 4.5, 8, 7.5, 6, 10, 3.9];

const reprovados = alunos.filter((alunos, indice) => medias[indice] < 7 );

console.log(`\nLista de Aprovados ${aprovados} \n`);
console.log(`Lista de Reprovados ${reprovados}\n`);
