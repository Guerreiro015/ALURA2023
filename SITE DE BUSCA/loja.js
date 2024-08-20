function Exibir(filtro) {
    fetch('http://makeup-api.herokuapp.com/api/v1/products.json')
        .then(res => res.json())
        .then((dados) => {
            const ul = document.getElementById('listaProdutos');

            ul.innerHTML = ""
            dados.map((key) => {
                if (key.name.toUpperCase().indexOf(filtro.toUpperCase()) >= 0 || filtro == "") {

                    const li = document.createElement('li');
                    li.innerHTML = `
                    <a href="#">   
                        <img width="200px" height="200px" src="${key.image_link}" alt="Foto Produto">                    
                        <span class="item-nome">Produto: ${key.name}</span>                                              
                        <span class="item-nome">Categoria: ${key.category}</span>                                              
                        <span class="item-nome">Lista: ${key.tag_list}</span>                                             
                        <span class="item-nome">Preço: ${key.price}</span>                                             
                                                           
                    </a>           
            `;
                    ul.appendChild(li);

                }
            });
        }
        )
}



// "id": 1048,
//         "brand": "colourpop",
//         "name": "Lippie Pencil",
//         "price": "5.0",
//         "price_sign": "$",
//         "currency": "CAD",
//         "image_link": "https://cdn.shopify.com/s/files/1/1338/0845/collections/lippie-pencil_grande.jpg?v=1512588769",
//         "product_link": "https://colourpop.com/collections/lippie-pencil",
//         "website_link": "https://colourpop.com",
//         "description": "Lippie Pencil A long-wearing and high-intensity lip pencil that glides on easily and prevents feathering. Many of our Lippie Stix have a coordinating Lippie Pencil designed to compliment it perfectly, but feel free to mix and match!",
//         "rating": null,
//         "category": "pencil",
//         "product_type": "lip_liner",
//         "tag_list": [
//             "cruelty free",
//             "Vegan"