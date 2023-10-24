const clientes = require("./dadosExercicioJSON.json");

//console.log(clientes);


const ordenar = clientes.sort(function ordem(a, b){
    if (a.nome < b.nome) return -1;
    if (a.nome > b.nome) return 1;
    return 0;
})

console.log(ordenar);

//////////////////////////////
let numeros =  [0, 20, 3, 4]
let teste = numeros.sort(function compare(a, b) {
if (a < b) return -1;
if (a > b) return 1;
return 0;
})
// dá [0, 3, 4, 20]

console.log(teste)

