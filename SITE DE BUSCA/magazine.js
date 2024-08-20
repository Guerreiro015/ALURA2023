function Exibir(filtro) {
    fetch('https://fakestoreapi.com/products')
        .then(res => res.json())
        .then((dados) => {
            const ul = document.getElementById('listaProdutos');

            ul.innerHTML = ""
            dados.map((key) => {
                if (key.title.toUpperCase().indexOf(filtro.toUpperCase()) >= 0 || filtro == "" || key.category.toUpperCase().indexOf(filtro.toUpperCase()) >= 0) {

                    const li = document.createElement('li');
                    li.innerHTML = `
                    <a href="#">
                        <img width="200px" height="200px" src="${key.image}" alt="">
                        <span class="item-nome">Produto: ${key.title}</span>
                        <span class="item-nome">Descrição: ${key.category}</span>
                        <span class="item-nome">Preço: ${key.price}</span>
                    </a>           
            `;
                    ul.appendChild(li);

                }
            });
        }
        )
}





