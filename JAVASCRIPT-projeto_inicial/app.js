alert('Boas-vindas ao jogo do número secreto');
let numeroSecreto = 10;
let chute
let tentativas=1
while(chute!=numeroSecreto){

    chute=prompt('Escolha um número entre 1 e 30');
    
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

         }
         tentativas ++
    }


