// O comando VAR difente de LET e const pode chamada antes de ser criada
// O comando VAR difente de LET e const pode atribuir valor mais de uma vez a uma variavel
// O comando CONST so consegue atribuir valor a uma variável uma vez
// O comando CONST NÃO consegue criar uma variavel sem valor


var alt = 5;
var lar = 6;
res = lar * alt;
console.log(res);

let altu = 5;
let larg = 7;
resu = larg * altu;
console.log(resu);

const al = 5;
const la = 8;
re = la * al;
console.log(re);

area = altu * alt
console.log(" Exemplo de VAR ...:  " + area) // exemplo de var atribuindo valor depois da varivael ser chamada.
var area;

let forma = "quadrado"
let desen = 'quadradO'
if (forma === desen) {
    console.log(al * la)
}
else {
    console.log(al * (la * 20))
}

// tipos de variveis

console.log(0 == false)
console.log("" == false)
console.log(1 == true)

//verificar o tipo de variavel
let str = "texto";
let num = 5;
let car;
let nul=null;

console.log('variavel str e uma '+typeof(str));
console.log('variavel num e uma '+typeof(num));
console.log('variavel car e uma '+typeof(car));
console.log('variavel nul e uma '+typeof(nul));






