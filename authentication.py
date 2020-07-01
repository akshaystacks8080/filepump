def saveUserInfoToFile(userdata):
    with open('userdata.txt', 'a+') as userDataFile:
        name = userdata['name']
        email = userdata['email']
        password = userdata['password']
        data = name + "\t" + email + "\t" + password + "\n"
        userDataFile.write(data)


def checkCredentials(userdata):
    status = False
    email = userdata['email']
    password = userdata['password']
    with open('userdata.txt', 'r') as checkDataFile:
        lines = checkDataFile.readlines()
        for line in lines:
            data = line.split("\t")
            curEmail = data[1]
            curPassword = data[2]
            curPassword = curPassword.strip()
            if email == curEmail and password == curPassword:
                status = True
    return status


def checkEmail(email):
    status = False
    try:
        dataFile = open("userdata.txt", "r")
        lines = dataFile.readlines()
        for line in lines:
            lineName, lineEmail, linePassword = line.split('\t')
        if email == lineEmail:
            status = True
        dataFile.close()
    except:
        print("Unable to read file")
    return status
