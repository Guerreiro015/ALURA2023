let dados = require("./dadosExercicioJSON.json");
 console.log(dados);
 console.log(dados[2]);
 console.log(dados[1].nome);

function encontrar(lista, chave, valor) {
    //return lista.find((item) => item[chave].includes(valor));
    console.log( lista.find((item) => item[chave].includes(valor)));
  }

//   const encontrado2 = encontrar(dados, "telefone", '47975323087');
//   const encontro = encontrar(dados, "nome", 'Izaak');
  


// console.log(encontrado2);
//   console.log(encontro);
encontrar(dados,'nome','Izaak')
encontrar(dados,"telefone", '47975323087')