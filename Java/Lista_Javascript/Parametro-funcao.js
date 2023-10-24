
function soma(num1,num2){
   total = num1*num2
    retorno = `A soma de ${num1} com ${num2} e exatamente ${total}`
console.log(retorno)
}

soma(5,10)

function somar(n1,n2){
    return n1+n2
}

function somar2(nu1,nu2){
   let toto =  nu1*nu2
   console.log(toto)
}

somar2(somar(5,5),somar(3,3))

function cumprimentar(){
    return 'Oi gente!'
   }
   
   function cumprimentaPessoa(nomePessoa) {
    console.log(`${cumprimentar()} Meu nome é ${nomePessoa}`)
   }
   
   cumprimentaPessoa('Paula') // “Oi gente! Meu nome é Paula”

