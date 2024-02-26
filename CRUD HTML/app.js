// Abrindo o banco de dados
var request = window.indexedDB.open("MeuBanco", 1);

request.onupgradeneeded = function(event) {
    // Aqui você pode criar tabelas, índices e popular o banco, se necessário
};

request.onsuccess = function(event) {
    // O banco de dados foi criado/aberto com sucesso
};

request.onerror = function(event) {
    // Ocorreu um erro ao criar/abrir o banco de dados
};



//Estruturando o Banco de Dados: Dentro do evento onupgradeneeded, você pode criar tabelas, definir índices e até mesmo popular o banco de dados com dados iniciais. Por exemplo:
request.onupgradeneeded = function(event) {
       var db = event.target.result;

       // Criando uma tabela
       var objectStore = db.createObjectStore("MinhaTabela", { keyPath: "id" });

       // Criando um índice
       objectStore.createIndex("nome", "nome", { unique: false });

       // Populando a tabela com dados iniciais
       objectStore.add({ id: 1, nome: "Alice" });
       objectStore.add({ id: 2, nome: "Bob" });
   };


  // Realizando Operações no Banco de Dados: Para adicionar, recuperar ou atualizar dados, você precisará iniciar uma transação e fazer uma solicitação. Por exemplo:
var transaction = db.transaction("MinhaTabela", "readwrite");
   var objectStore = transaction.objectStore("MinhaTabela");

   // Adicionando um novo registro
   objectStore.add({ id: 3, nome: "Carlos" });

   // Obtendo um registro pelo ID
   var getRequest = objectStore.get(1);
   getRequest.onsuccess = function(event) {
       var data = event.target.result;
       console.log("Nome encontrado:", data.nome);
   };
