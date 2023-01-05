const User = require('../../model/User');

//Register a new user
const registerUser = async (req, res)=>{
    const {email, firstname, lastname, password} = req?.body;
    try {
        //check if user exist 
        const userExist = await User.findOne({email});
        if(userExist){
            res.json('User already exist');
        }
        const user = await User.create({email, firstname, lastname, password});
        res.status(200).json(user);
    } catch (error) {
        res.json(error);
    }
};

module.exports = {registerUser}