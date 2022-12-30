const mongose = require('mongoose');

//schema for user
const userSchema = new mongose.Schema({
    firstname: {
        required: [true, 'First name is required'],
        type: String,
    },
    lastname: {
        required: [true, 'Last name is required'],
        type: String,
    },
    email: {
        required: [true, 'Email is required'],
        type: String,
    },
    password: {
        required: [true, 'Password is required'],
        type: String,
    },
    isAdmin: {
        type: Boolean,
        default: false,
    }
}, {
    timestamps: true,
});

//compile schema into model
const User = mongose.model('User', userSchema);
model.exports = User;