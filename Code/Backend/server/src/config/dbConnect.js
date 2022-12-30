const mongoose = require('mongoose');
const dbConnect = async() => {
    try{
        await mongoose.connect("mongodb+srv://admin:ro58N0aLKXYIV03A@fintap.s5iji7j.mongodb.net/?retryWrites=true&w=majority", {
            useUnifiedTopology: true,
            useNewUrlParser: true
        });
        console.log("MongoDB connected successfully");

    } catch (error){
        console.log(`Error ${error.message}`);
    }
}

module.exports = dbConnect;


//MongoDB Database User Details
//Username: admin
//Password: ro58N0aLKXYIV03A
//mongodb+srv://admin:<password>@fintap.s5iji7j.mongodb.net/?retryWrites=true&w=majority

