// ( .includes)verificar se está dentro da lista ()
// indexOf = mostra o posição do item na lista


var alunos = ["João", "Juliana", "Ana", "Caio"];
var notas = [10, 8, 7.5, 9];

let escola = [alunos, notas];

function procura(nome) {
    if (escola[0].includes(nome)) {

        indice = escola[0].indexOf(nome)

        med = escola[1][indice]
        console.log(`O( aluno ${nome} está matriculado e sua média anual é ${med}`);


    }
    else {
        console.log(`O aluno ${nome} NÃO está matriculado nesta escola`);

    }

}

procura("Juliana");
