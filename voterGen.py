#import pickle,csv, names, uuid, random
import csv
from helper import *
# sex = ["M", "F", "Other"]

# def genVoter(n, uAge=18, lAge=100, ):

#     voters = []
#     for i in range(n):
#         vID = str(uuid.uuid4()).split("-")[0]
#         vName = names.get_full_name()
#         vAge = random.randint(uAge,lAge)
#         vSex = random.choice(sex)
#         voters.append([vID,vName,vAge,vSex])
#     return voters

# def dep(voters):
#     with open("voterList.csv", "w") as f:
#         wO = csv.writer(f)
#         wO.writerow(["Name", "Age", "Sex"])
#         for i in voters:
#             wO.writerow(i[1:])

#     with open("voterList.dat", 'wb') as f:
#         for i in voters:
#             pickle.dump({"ID":i[0], "Name":i[1]}, f)

# dep(genVoter(50))
# data = fetchVoters()
# formattedData = []
# for i in data:
#     formattedData.append(i+["N"])                     added Voted attribute
# with open("Data/VoterList.csv", 'w') as f:
#     writer = csv.writer(f)
#     writer.writerows(formattedData)

# data = fetchVoters()
# data1 = fetchVotersBIN()
# values = []
# formattedData = []
# for i in data1:
#     values.append(i[0])
# for i in range(len(data)):
#     formattedData.append([values[i]]+data[i])

# with open("Data/VoterList.csv", 'w') as f:
#     writer = csv.writer(f)
#     writer.writerows(formattedData)