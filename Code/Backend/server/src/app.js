const express = require('express');
const dbConnect = require('./config/dbConnect');
const { registerUser } = require('./controllers/users/usersCtrl');

const { errorHandler, notFound } = require('./middlewares/errorMiddleware');
const userRoute = require('./routes/users/usersRoute');
const app = express();



//dbConnect
dbConnect();

//middlewares
//body parser
app.use(express.json()); 


//routes
app.use('/', userRoute);

//Error
app.use(notFound);
app.use(errorHandler);


module.exports = app;





