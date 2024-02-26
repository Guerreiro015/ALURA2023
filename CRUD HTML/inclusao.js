const request = window.indexedDB.open("MeuBancoDeTeste", 3);

   request.onsuccess = function () {
     console.log("Banco de dados aberto com sucesso");
     const db = request.result;
     const transaction = db.transaction("carros", "readwrite");
     const store = transaction.objectStore("carros");

     // Exemplo: Adicionando dados à loja de objetos
     store.put({ id: 1, cor: "Vermelho", marca: "Toyota" });
     store.put({ id: 2, cor: "Vermelho", marca: "Kia" });
     store.put({ id: 3, cor: "Azul", marca: "Honda" });
     store.put({ id: 4, cor: "Prata", marca: "Subaru" });

     // Exemplo: Recuperando dados da loja de objetos
     const idQuery = store.get(4);
     const corQuery = store.index("carros_cor").getAll(["Vermelho"]);
     const corEMarcaQuery = store.index("cor_e_marca").get(["Azul", "Honda"]);

     idQuery.onsuccess = function () {
       console.log("Resultado da consulta por ID:", idQuery.result);
     };
     corQuery.onsuccess = function () {
       console.log("Resultado da consulta por cor:", corQuery.result);
     };
     corEMarcaQuery.onsuccess = function () {
       console.log("Resultado da consulta por cor e marca:", corEMarcaQuery.result);
     };

     transaction.oncomplete = function () {
       db.close();
     };
   };

   