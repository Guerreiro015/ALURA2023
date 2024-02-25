
function exibirTextoNaTela(tag, texto) {
    let titulo = document.querySelector(tag);
    titulo.innerHTML = texto;
}

exibirTextoNaTela("h1", 'Jogo do amigo secreto')
exibirTextoNaTela("p", 'Escolha um número de 1 a 10')
let numero = gerarNumeroAleatorio()

function gerarNumeroAleatorio() {
    return parseInt(Math.random() * 10 + 1)
}


contador=0
function verificarChute() {
    let chutar = document.querySelector('input').value
    let chute = parseInt(chutar)
    // let numero = gerarNumeroAleatorio()
    if (chute > numero) {

        exibirTextoNaTela("p", 'O Chute é Maior que o Número Secreto')
    }
    else if (chute < numero) {
        exibirTextoNaTela("p", 'O Chute é Menor que o Número Secreto')
    }
    else {
        exibirTextoNaTela("p", 'Acertou o número secreto é ' + numero + contador)
        document.getElementById('reiniciar').removeAttribute('disabled');

    }
    contador++
}

function novo_jogo(){
    contador=1
    numero = gerarNumeroAleatorio();
    exibirTextoNaTela("p", 'Escolha um número de 1 a 10')
    chutar = document.querySelector('input')
    chutar.value=""
    document.getElementById('reiniciar').setAttribute('disabled',true);

    
}










