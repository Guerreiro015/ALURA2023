//Arrows functions e muito parecido e se comporta como a expressão-função
//Ambos são utilizados para diminuir o tamanho do código.

function apresentar(nome) {
    return `Meu nome é ${nome} `;
}
apresentar('Antonio')

//arrows-functions

const apresentararrows = nome => `Meu nome é ${nome}`;
const soma = (nu1, nu2) => nu1 + nu2;

console.log(soma(4,8));

//arrows-functions com mais de 1 linha de instrução

const somar = (nu1, nu2) => {
    if (nu1 > 10 || nu2 > 10){
        return "somente numeros de 01 a 09"
    }
     else{
        return nu1+nu2;
    }
}
console.log(somar(5,6));


