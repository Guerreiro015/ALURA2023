

var items = [];

document.querySelector('input[type=submit]').addEventListener('click', () => {
    var nomeProduto = document.getElementById(id = 'nome-produto')
    var valorProduto = document.getElementById(id = 'valor-produto')

    items.push({ nome: nomeProduto.value, valor: valorProduto.value })
    /*
    <div class="lista-produtos-single">
                <h3>Red bull</h3>
                <h3 class="price">R$ 20,00</h3>
            </div>
    
    */

    let listaProdutos = document.querySelector('.lista-produtos');
    let soma = 0

    listaProdutos.innerHTML = "";

    items.map(function (val) {
        soma += parseFloat(val.valor)
        listaProdutos.innerHTML += `        
        <div class="lista-produtos-single">
        <h3>`+ val.nome + `</h3>
        <h3 class="price">R$ `+ val.valor + `</h3>
        </div>  

        `;

    })
    nomeProduto.value = ''
    valorProduto.value = ''
    soma=soma.toFixed(2)
    let elementoSoma=document.querySelector('.soma-produto')
    elementoSoma.innerHTML='Total:  R$:'+soma

    document.querySelector('.limpar').addEventListener('click',()=>{
        items=[]
        soma=0
        listaProdutos.innerHTML = "";
        elementoSoma.innerHTML=''
    })

})

