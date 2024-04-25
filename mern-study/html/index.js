const express = require("express");
const path = require("path");
const mysql = require("mysql2");

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const conn = mysql.createConnection({host : "localhost", user : "root", password : "1234", database : "mern"});

conn.connect((err) => {
    if(err){
        console.log(err)
    }
});

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "public/index.html"));
});

app.get("/auth", (req, res) => {
    res.sendFile(path.join(__dirname, "public/auth.html"));
});

app.post("/signup", (req, res) => {
    const data = req.body;
    let sql = "INSERT INTO user SET ?";
    conn.query(sql, data, (err, result)=>{
        if (err) res.json({ status: false });
        console.log(result);
        res.json({ status: true });
    });
});


app.post("/login", (req, res) => {
    const { email, password } = req.body;
    const sql = `SELECT * FROM user WHERE email = ? AND password = ?`;
    conn.query(sql, [email, password], (err, result) => {
        if (err || result.length <= 0) {
            return res.json({ status: false });
        }else {
            return res.json({ status: true });
        }
    });
});



app.listen(2004, () => {
    console.log("Running on Port 2004");
});
