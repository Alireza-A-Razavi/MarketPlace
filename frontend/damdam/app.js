const path=require("path")
const express=require('express')
const b=require("body-parser")
const app=express()
var EJS  = require('ejs');
app.set("view engine",'ejs')
app.set('views', 'views')
app.use(b.urlencoded({ extended: false }))
app.use(express.static(__dirname + '/public'));
const r=express.Router()
app.get("/",(req,res)=>{
    res.render("index")
})
app.get("/userPanel",(req,res)=>{
    res.render("userPanel")
})
app.get("/userPanel/createProduct",(req,res)=>{
    res.render("userPanel")
})

app.get("/singleProduct",(req,res)=>{
    res.render("product")
})
app.get("/products",(req,res)=>{
    res.render("products")
})

app.get("/signin",(req,res)=>{
    res.render("signin")
})

app.get("/signup",(req,res)=>{
    res.render("signup")
})
app.post('/testy',(req,res)=>{
    console.log(req.body)
})



app.listen(3000)