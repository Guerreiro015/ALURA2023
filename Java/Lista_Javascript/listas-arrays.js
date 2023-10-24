const nota1 = 10;
const nota2 = 6.5;
const nota3 = 8;
const nota4 = 7.5;

const media = (nota1 + nota2 + nota3 + nota4) / 4;

console.log(media);

let notas = [10, 6.5, 8, 7.5];

let medias = (notas[0] + notas[1] + notas[2] + notas[3]) / notas.length;

console.log(medias);


console.log(`Minha lista de notas normal...............:     ${notas}
`);

//Adicionar elementos na arrays ou lista ( usar .push() )

notas.push(10, 9);
console.log(`Minha lista de notas adicionando mais itens     ${notas}
`);

//deletando o último elementos na arrays ou lista ( usar .pop() )

notas.pop()
console.log(`Minha lista de notas retirando o último itens . ${notas}
`);

//deletando o primeiro elementos na arrays ou lista ( uasr .shift() )

notas.shift()
console.log(`Minha lista de notas retirando o primeiro itens  ${notas}
`);

//juntando duas litas ( uasr .pop() )
no = [3,4.5]

juntar = notas.concat(no)
console.log(`Minha lista de notas juntando outra lista.....:  ${juntar}
`);

console.log(juntar);











