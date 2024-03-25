async function connect(){
    if(global.connection && global.connection.state !== 'disconnected')
        return global.connection;
 
    const mysql = require("mysql2/promise");
    const connection = await mysql.createConnection("mysql2://root:Lucas@0108@localhost:3306/teste");
    console.log("Conectou no MySQL!");
    global.connection = connection;
    return connection;
}



async function selectCustomers(){
    const conn = await connect();
    const [rows] = await conn.query('SELECT * FROM usuarios;');
    return rows;
}



async function insertCustomer(customer){
    const conn = await connect();
    const sql = 'INSERT INTO usuarios(nome,email,senha,idade,createdAt,updatedAt) VALUES (?,?,?,?,?,?)'
    const values = [customer.nome, customer.email, customer.senha, customer.idade,customer.createdAt,customer.updatedAt];
    return await conn.query(sql, values);
}




async function updateCustomer(id, customer){
    const conn = await connect();    
    const sql = 'UPDATE usuarios SET nome=? ,email=? ,senha=? ,idade=? ,createdAt=? ,updatedAt=? WHERE id=?'
    const values = [customer.nome, customer.email, customer.senha, customer.idade,customer.createdAt,customer.updatedAt, id];
    return await conn.query(sql, values);
}

1

async function deleteCustomer(id){
    const conn = await connect();
    const sql = 'DELETE FROM usuarios where id=?;';
    return await conn.query(sql, [id]);
}
 
module.exports = {selectCustomers, insertCustomer, updateCustomer, deleteCustomer}

