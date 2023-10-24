
//  Vamos coolocar um função dentro do objeto


const objeto = {
    nome: 'antonio',
    idade: 58,
    cpf: '112233444',
    email: 'antonio@gmail.com',
    saldo: 200,

    compra: function (valor) {
        // O complemento this é usado para chamar uma propiedade dentro do objeto
        if (this.saldo < valor) {
            let restante = valor - this.saldo
            console.log(`\nO seu saldo não é suficiente faltou ${restante} reais\n`);
        }
        else {
            let restante = this.saldo - valor;
            console.log(`\nCompra realizada com sucesso seu novo saldo é de ${restante} reais\n`)
        }
    }

}


objeto.compra(45)
