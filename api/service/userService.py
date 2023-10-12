from flask import request, Blueprint, jsonify



userEndpoint = Blueprint('user', __name__)

SUCESS = "Sucess"
FAILURE = "Failure"

@userEndpoint.route("/get-users", methods = ['GET'])
def get_users():
    from dbFactory.userFactory import getAllUserData
    userList = getAllUserData()

    if userList == -1:
        return jsonify(FAILURE + ": no users found "), 500
    else:
        return jsonify(userList), 200

@userEndpoint.route("/", methods = ['GET'])
def test():
    return "test"

@userEndpoint.route("/get-user/<user_id>", methods = ['GET'])
def get_user(user_id):
    from dbFactory.userFactory import getUserData
    userList = getUserData(user_id)

    if userList == -1:
        return jsonify(FAILURE + ": no user of id " + user_id), 500
    else:    
        return jsonify(userList), 200

@userEndpoint.route("/create-user", methods = ['POST'])
def create_user():
    
    #gets Query params
    email = request.args.get("email")
    firstName = request.args.get("firstName")
    lastName = request.args.get("lastName")
    password = request.args.get("password")

    user_data = {
        "firstName": firstName,
        "lastName": lastName,
        "email": email,
        "password": password
    }

    responseString = validateUserData(user_data)
    if responseString == SUCESS:
        from dbFactory.userFactory import saveUserData
        saveUserData(email, firstName, lastName, password)
        return jsonify(responseString), 200
    else:
        return jsonify(responseString), 500



def validateUserData(user_data):

    if user_data["email"] is None:
        return "Required Email"
    elif user_data["firstName"] is None:
        return "Required firstName"
    elif user_data["lastName"] is None:
        return "Required lastName"
    elif user_data["password"] is None:
        return "Required password"
    else:
        return SUCESS

