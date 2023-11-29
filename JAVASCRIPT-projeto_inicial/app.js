alert('Boas-vindas ao jogo do número secreto');

// parseInt = parte inteira
const valor=200
let numeroSecreto = parseInt(Math.random()*valor+1)
let chute
let tentativas=1
while(chute!=numeroSecreto){

    chute=prompt(`Escolha um número entre 1 e ${valor}`);
    
    if(numeroSecreto==chute){

        alert(`Isso aí! você descobriu em ${tentativas} tentativas, o número secreto é ${numeroSecreto}`);
        break
    }

    else{
        if(chute>numeroSecreto){
            alert(`O numero secreto é menor que ${chute} chutado `)
            
        }
        else{
            
            alert(`O numero secreto é maior que ${chute} chutado `)
        }

        tentativas ++
         }
    }


