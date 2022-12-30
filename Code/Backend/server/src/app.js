const express = require('express');
const dbConnect = require('./config/dbConnect');
const app = express();

//dbConnect
dbConnect();

module.exports = app;



