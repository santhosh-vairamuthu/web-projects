const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql2');

const app = express();
const port = 8080;

const dbConfig = {
    host: 'localhost',
    user: 'root',
    password: '1234',
    database: 'node'
};
const pool = mysql.createPool(dbConfig);
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});
app.post('/saveToDb', (req, res) => {
    const name = req.body.name;
    const age = req.body.age;
    pool.getConnection((err, connection) => {
        if (err) {
            console.error('Error getting MySQL connection:', err);
            res.status(500).send('Internal Server Error');
            return;
        }
        const query = 'INSERT INTO t1 (name, age) VALUES (?, ?)';
        const values = [name, age];

        connection.query(query, values, (err, result) => {
            connection.release();

            if (err) {
                console.error('Error executing MySQL query:', err);
                res.status(500).send('Internal Server Error');
                return;
            }

            console.log('Data saved to MySQL database:', result);
            res.status(200).send('Data saved to database');
        });
    });
});
app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}/`);
});
