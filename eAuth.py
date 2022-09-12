# imports
import pickle, caesarCipher, csv

#---------------------------------------------------------Logins----------------------------------------------------------

def adminLogin(): #Admin login details check
    adminName = input("Admin Name: ")
    adminPassword = input("Password: ")
    f = open("Data/cred.dat", "rb")
    try:
        while True:
            data = pickle.load(f)
            if adminName == caesarCipher.caesarDecrypt(data['Admin Name']) and adminPassword == caesarCipher.caesarDecrypt(data["Password"]):
                f.close() 
                return (True,adminName)
    except EOFError:
        f.close() 
        return (False,)


def voterLogin(): #Checks whether the VOTER'S name and UID exists within the database and correspond to each other
    ID = input("ID: ")
    name = input("Name: ")
    f = open("Data/voterList.csv", 'r')
    reader = csv.reader(f)
    for i in reader:
        if ID == i[0] and name == i[1]:
            f.close()
            return True
    f.close()
    return False
    # try:
    #     while True:
    #         voterData = pickle.load(votersFile)
    #         if voterData["Name"] == name and voterData["ID"] == ID:
    #             votersFile.close()
    #             return True
    # except EOFError:
    #     votersFile.close()
    #     return False

#^-------------------------------------------------------^Logins^--------------------------------------------------------^
