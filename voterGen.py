import pickle,csv, names, uuid, random
import csv
from helper import *

sex = ["M", "F", "Other"]

def genVoter(n, lAge=18, uAge=100, ):

    voters = []
    for i in range(n):
        vID = str(uuid.uuid4()).split("-")[0]
        vName = names.get_full_name()
        vAge = random.randint(lAge,uAge)
        vSex = random.choice(sex)
        voters.append([vID,vName,vAge,vSex,"N"])
    return voters

def dep(voters):
    with open("voterList.csv", "w", newline="") as f:
        wO = csv.writer(f)
        wO.writerow(["ID", "Name", "Age", "Sex", "Voted"])
        for i in voters:
            wO.writerow(i)

dep(genVoter(50))
