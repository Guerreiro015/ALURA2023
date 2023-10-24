let objeto = {
nome:'antonio',
idade: 58,
cpf: '112233444',
email: 'antonio@gmail.com'};


console.log ("\n");
console.log (objeto);
console.log ("\n");
console.log (objeto.nome,objeto.idade);

console.log (`\n O nome do aluno é ${objeto.nome} e sua idade é ${objeto.idade} anos\n`);

console.log (`\n Os três primeiros numeros do cpf são ${objeto.cpf.substring(0,3)}\n`);




const cliente = {
    nome: "Andre",
    idade: 32,
    cpf: "1122233345",
    email: "andre@dominio.com",
  };
  
  console.log(
    `O nome do cliente é ${cliente["nome"]} e essa pessoa tem ${cliente["idade"]} anos.`
  );
  
  const chaves = ["nome", "idade", "cpf", "email", "altura"];
  
  chaves.forEach((chave) => {
    console.log(`A chave ${chave} tem valor ${cliente[chave]}`);
  });

  chaves.forEach((marca) =>{
    console.log(`\n A chave ${marca} tem valor ${objeto[marca]}`)
  })

 


