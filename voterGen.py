import pickle,csv, names, uuid, random

sex = ["M", "F", "Other"]

def genVoter(n, uAge=18, lAge=100, ):

    voters = []
    for i in range(n):
        vID = str(uuid.uuid4()).split("-")[0]
        vName = names.get_full_name()
        vAge = random.randint(uAge,lAge)
        vSex = random.choice(sex)
        voters.append([vID,vName,vAge,vSex])
    return voters

def dep(voters):
    with open("voterList.csv", "w") as f:
        wO = csv.writer(f)
        wO.writerow(["Name", "Age", "Sex"])
        for i in voters:
            wO.writerow(i[1:])

    with open("voterList.dat", 'wb') as f:
        for i in voters:
            pickle.dump({"ID":i[0], "Name":i[1]}, f)

dep(genVoter(50))
