var db = openDatabase('meubanco','2.0','Mybase',4048);
db = transaction(function(criar){
    criar.executeSql('IF NOT EXIST CREATE TABLE usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, senha TEXT')
})
