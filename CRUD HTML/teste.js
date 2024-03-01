const sqlite3 = require('sqlite3').verbose();

const db = new sqlite3.Database('meu_banco_de_dados.db');

db.run('CREATE TABLE usuarios (nome TEXT, email TEXT, idade INTEGER)');

db.run(`INSERT INTO usuarios (nome, email, idade) VALUES ('João', 'joao@example.com', 25)`);