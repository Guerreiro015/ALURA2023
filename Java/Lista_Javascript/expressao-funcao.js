//Arrows functions e muito parecido e se comporta como a expressão-função
//Ambos são utilizados para diminuir o tamanho do código.


//Expressão de função - colocamos a função variavel e valor da variavel na mesma linha.
const soma = function (n1 = 1, n2 = 3) { return n1 + n2 }
console.log(soma())
console.log(soma(3, 5))

