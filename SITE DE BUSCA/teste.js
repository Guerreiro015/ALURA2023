fetch('banco.json')
            .then(res => res.json())
            .then((dados) => {
                for (key in dados){
                    console.log(key)
                }
            })


            const chaves = Object.keys(meuObjeto);
console.log(chaves); // ["nome", "idade", "cidade"]