import csv, names, uuid, random, lorem

symbols = ['☀︎', '☽', '☁︎', '☕︎', '✂︎', '⚚', '☭', '☯︎', '☮︎', '♞']
sex = ["M", "F", "Other"]

def genCand(n=10, uAge=18, lAge=100, ):

    candidates = []
    if n >10:
        return "Max candidate capacity reached"
    else:
        for i in range(n):
            cID = str(uuid.uuid4()).split("-")[0]
            cName = names.get_full_name()
            cAge = random.randint(uAge,lAge)
            cSex = random.choice(sex)
            cSymbol = random.choice(symbols)
            symbols.remove(cSymbol)
            desc = lorem.sentence()
            candidates.append([cID,cName,cAge,cSex,cSymbol,desc])
    return candidates

candidates = genCand()

def dep():
    with open("candidateList.csv", 'w', newline="") as f:
        w_o = csv.writer(f)
        w_o.writerow(["ID", "Name", "Age", "Sex", "Symbol", "About" ])
        w_o.writerows(candidates)
