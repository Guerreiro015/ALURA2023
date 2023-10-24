
// O for para usar com objeto
const pessoa = {
    nome:"Bruce Banner",
    dataNascimento:"25/01/1980",
    identidade:"997776-X",
    email:"profbanner@email.com",
    telefone:"+552877776666",
    cidade:"Cachoeiro de Itapemirim",
    estado:"ES"
 }

 pessoa.endereco = {
 rua: 'miguel francisco',
 numero: 123,
 bairro: 'tapioca' };

 console.log(pessoa);

 // modelos do for

 // Mostrar os objetos  (pecorrer todods os objetos)

for(let ob in pessoa){
   console.log("\n"+ob)//mostrar os objetos
   }

 for(let ob in pessoa){
    console.log(pessoa[ob])//mostrar o conteudo dos objetos
 }
 
 for(let ob in pessoa){
 console.log( `\n Campo ${ob} contem a informação ${pessoa[ob]} \n`)
 }




 for(let campo in pessoa){

    let tipo = typeof pessoa[campo];
   
    // campo diferenete de objeto ou funçao ele executa o console

    if (tipo !== "object" && tipo !== "function"){

    /// Nao podemos usar pessoa.campo temos que usar pessoa[campo]
    console.log(` \n No campo ${campo} contém o valor ${pessoa[campo]}\n`);
 }
}
