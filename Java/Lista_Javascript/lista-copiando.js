const sala1 = [6, 7, 8, 10, 4];

let copia = sala1;

copia.push(20)
sala1.push(5)

console.log(`Copia é igual a ${copia}\n`);
console.log(`Sala1 é igual a ${sala1}\n`);
/// Quando colocamos um variavel igual a outra tudo que uma mudar a outra também muda

//Resolvendo apenas colocar como lista e colocar reticensias ...

let copp = [...sala1];
let copiy = [3,...sala1,20];

copp.push(1000)

console.log(`Copia correta é igual a ${copiy}\n`);
console.log(`Copia correta é igual a ${copp}\n`);
