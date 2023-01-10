const expressAsyncHandler = require("express-async-handler")
const User = require('../../model/User');

//Register a new user
const registerUser = expressAsyncHandler(async (req, res)=>{
    const {email, firstname, lastname, password} = req?.body;
    
    //check if user exist 
    const userExist = await User.findOne({email});
    if(userExist) throw new Error('User already exist');

    try {
        const user = await User.create({email, firstname, lastname, password});
        res.status(200).json(user);
    } catch (error) {
        res.json(error);
    }
});

module.exports = {registerUser}