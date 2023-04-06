const expressTypes = require("express");
const operations = require('./operations');

function delay(time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}

// define the controller
const controller = {
  hello: (
    /** @type {expressTypes.Request} */ req,
    /** @type {expressTypes.Response} */ res
  ) => {
    // call the model
    const data = { data: "Hello World!" };
    // send the response
    res.send(data);
  },
  isLoggedIn: async (
    /** @type {expressTypes.Request} */ req,
    /** @type {expressTypes.Response} */ res,
    next
  ) => {
    // await delay(1000);
        var token =  req.query.token;
  if (!token) {
    return res.status(400).json({
      error: true,
      message: "Token is required."
    });
  }
  // check token that was stored
  let check = await operations.verifyTok(token);
    if (!check.auth){
        return res.status(401).json({
        error: true,
        message: "Invalid token."
    });
    }
   
    // get basic user details
    req.body.username = check.username;
    next()
  },
  verifyToken: async (
    /** @type {expressTypes.Request} */ req,
    /** @type {expressTypes.Response} */ res
  ) => {
    var token =  req.query.token;
  if (!token) {
    return res.status(400).json({
      error: true,
      message: "Token is required."
    });
  }
  // check token that was stored
  let check = await operations.verifyTok(token);
    if (!check.auth){
        return res.status(401).json({
        error: true,
        message: "Invalid token."
    });
    }
   
    // get basic user details
    var userObj = await operations.getCleanUser(check.username);
    return res.json({ user: userObj, token });
  },
  login: async (
    /** @type {expressTypes.Request} */ req,
    /** @type {expressTypes.Response} */ res
  ) => {

    console.log(req.body)
    const user = req.body.username;
    const pwd = req.body.password;
    
    // return 400 status if username/password does not exist
    if (!user || !pwd) {
        return res.status(400).json({
        error: true,
        message: "Username or Password required."
        });
    }

     //get password for the user
    const userData = await operations.checkUser(user)
    console.log(userData.password)
    // return 401 status if the credential is not match.
    if (user !== userData.username || pwd !== userData.password) {
        return res.status(401).json({
        error: true,
        message: "Username or Password is Wrong."
        });
    }
    
    // generate token
    const token = operations.generateToken(userData);
    // get basic user details
    const userObj = await operations.getCleanUser(userData.username);
    // store token of current user
    operations.storeTok(token,userData.username)
    // return the token along with user details
    return res.json({ user: userObj, token });
  },
  fetchBalance: async (
    /** @type {expressTypes.Request} */ req,
    /** @type {expressTypes.Response} */ res
  ) => {
    let { username } = req.body;

    
  },
  
};

// export the controller
module.exports = controller;

// select cast(substring_index ("-7,0",',',1) AS int)+5 AS STRING;
