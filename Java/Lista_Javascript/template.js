let apelido = "antonio"
let idad = 2023 - 1972
let cidade = 'Imhuma-PI'

let normal = 'Meu nome é ' + apelido + " minha idade é " + idad + ' anos, Nasci em ' + cidade


// TEMPLATE LATERAL - abrir a variavel com ( `TEXTO´ crase para (À))  e Usar cifrão antes da variavel 

let simplicado = `Meu nome é ${apelido} minha idade é ${idad} anos E nasci em ${cidade}`

console.log("---")
console.log(normal)
console.log("---")
console.log(simplicado)
console.log("---")


const nome = "Leo";
const idade = 18;
const bebidaMaior = "cerveja";
const bebidaMenor = "suco";

const pedido = `${nome} diz: "por favor, quero beber ${idade >= 18 ? bebidaMaior : bebidaMenor}"`
console.log(pedido)
console.log("---------------")
