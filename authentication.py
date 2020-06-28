def saveUserInfoToFile(userdata):
    with open('userdata.txt', 'a+') as userDataFile:
        name = userdata['name']
        email = userdata['email']
        password = userdata['password']
        data = name + "\t" + email + "\t" + password
        userDataFile.write(data)
