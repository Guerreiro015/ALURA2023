let numero = 1234
let texto = "1234"
let soma = Number(texto)
let resultaldo  = numero+texto

console.log(resultaldo)
console.log(numero+soma)

let telefone = 12341234;
console.log("O telefone é " + String(telefone)); // teremos a conversão do número 12341234 para uma string “12341234” e assim poderemos fazer a concatenação entre as strings

let tel = 12341234;
console.log("O tel é " + tel.toString()); // o .toString() é uma outra forma para  fazer essa conversão, que é mais parecida com outras linguagens de programação.

let usuarioConectado = false;
console.log(String(usuarioConectado)); // teremos a conversão da booleana para string, nesse caso teremos uma string “false”.

usuarioConectado = true;
console.log(String(usuarioConectado)); // agora teremos uma string “true”.

//Podemos usar o operador de soma + para fazer a conversão de textos para números, colocando-os antes das variáveis:

let largura = "10";
let altura = "5";
console.log( + largura * + altura); // teremos a conversão de String para números realizado usando o + antes das variáveis

