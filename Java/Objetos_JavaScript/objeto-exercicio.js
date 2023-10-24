
//Usando a representação do objeto pessoa, foi solicitado que adicionássemos os campos seguro social e cpf no formato string. Além disso, quando forem exibidas as informações da pessoa em um relatório, deverão aparecer somente os 4 primeiros dígitos do CPF e da carteira de identidade.

//Sabendo disso, analise as afirmações abaixo e selecione a verdadeira:


const pessoa = {
    nome:"Bruce Banner",
    dataNascimento:"25/01/1980",
    identidade:"997776-X",
    email:"profbanner@email.com",
    telefone:"+552877776666",
    cidade:"Cachoeiro de Itapemirim",
    estado:"ES"
 }

 console.log(pessoa);

 // Adicionar campos
 pessoa.seguro_social = "123.113.122223"
 //Outra maneira de incluir
 pessoa["cpf"] = "123.444.333-55"

 console.log(pessoa);

 console.log(` \nOs quatros primeiros digitos do cpf são ${pessoa.cpf.substring(0,4)}`)
 
console.log(`\nOs quatros primeiros digitos da identidade são ${pessoa.identidade.substring(0,4)}`)

// um ojeto com mais de item por item

pessoa['celular'] = ['999','8888','1111']
pessoa.filhos = ['antonio','luana','lucas']
delete pessoa.dataNascimento;

console.log(pessoa);


 