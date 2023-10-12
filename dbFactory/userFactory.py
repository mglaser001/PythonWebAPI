from werkzeug.security import generate_password_hash, check_password_hash

def saveUserData(email,firstName,lastName,password):
    from userModel import User
    newUser = User(email = email, firstName = firstName, lastName=lastName, password=generate_password_hash(password, method='sha256'))
    import app
    app.db.session.add(newUser)
    app.db.session.commit()

def getUserData(userId):
    from userModel import User
    import app

    user = User.query.filter_by(id).first()
    if user:
        return user
    else:
        return -1
    
def getAllUserData():
    from userModel import User
    import app

    users = User.query
    if users:
        return users
    else:
        return -1