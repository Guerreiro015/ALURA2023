let banco = {
nome: "ana",
idade: 19,
telefone: "1.9999.5555",
cpf: "123.123.123-23"}

// exibir um item do objeto
console.log(`\n O nome cadastrado é ${banco.nome}`)
console.log(`\n O nome cadastrado é ${banco.telefone}`)
// alterar um item do objeto ( Muito simples)
banco.nome = "Ana Maria de Sousa"
banco.telefone = '9.0000.1111'
console.log(`\n O nome alterado é ${banco.nome}`)
console.log(`\n O telefone alterado é ${banco.telefone}`)

// Incluir um item no objeto ( Muito simples)

banco.email = "antonoo@gmeail.ocm"



console.log(banco)

// deletar um item ( Muito fácil vamos deletar idade)

delete banco.idade

console.log(`\nVejamos com ficou o objeto deletando o item idade`)

console.log(banco)

