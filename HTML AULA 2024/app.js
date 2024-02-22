// let titulo = document.querySelector('h1');
// titulo.innerHTML = 'Jogo do número secreto';

// let paragrafo = document.querySelector('p');
// paragrafo.innerHTML = 'Escolha um número de 1 a 10'

function verificarChute() {
    alert('Botão Clicado')
}

function exibirTextoNaTela(tag, texto) {
    let titulo = document.querySelector(tag);
    titulo.innerHTML = texto;
}

exibirTextoNaTela("h1", 'Jogo do amigo secreto')
exibirTextoNaTela("p", 'Escolha um número de 1 a 10')

function gerarNumeroAleatorio() {
    return parseInt(Math.random() * 10 + 1)
}

numero=gerarNumeroAleatorio()
exibirTextoNaTela("p", numero)
