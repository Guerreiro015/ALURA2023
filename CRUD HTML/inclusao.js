let nomes = document.getElementById('nome').value
let senhas = document.getElementById('senha').value

var db = openDatabase('meu_banco')
db = transaction(function(incluir){
    incluir.executeSql("INSERT INTO usuarios(nome,senha) VALUES(?,?)",[nomes,senhas])
})
