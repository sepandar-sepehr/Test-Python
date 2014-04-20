import csv
with open('fellows.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    fellows = []
    for row in reader:
        print ', '.join(row)
        fellows.append(row[0])
        
with open('referrals.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    users = []
    referrals = []
    for row in reader:
        print ', '.join(row)
        users.append(row[0])
        referrals.append(row[1])

## === Part 1 ===
def FellowReffer(fellows,users,referrals):
    sf=0
    for f in fellows:
        for i in range(0,len(users)):
            if f == users[i] and referrals[i]!='':
                sf = sf+1
    return float(sf)/len(fellows)

## === Part 2 ===
def ViralCoef(fellows,users,referrals):
    refs=[]
    for u in users:
        i=0
        for r in referrals:
            if u==r:
                i=i+1
        refs.append(i)
    return float(sum(refs))/len(refs)

## === Part 3 ===
def AveRef(users,referrals):
    i=0
    for u in users:
        i=i+refsNo(u,users,referrals)
    return float(i)/len(users)

def refsNo(user,users,referrals):
    i=0
    for idx in range(len(referrals)):
        if user == referrals[idx]:
            i=i+1+refsNo(users[idx],users,referrals)
    return i

## === Part 4 ===
def aggrDollar(fellows,users,referrals):
    dollar=0
    reward=1024
    for f in fellows:
        dollar=dollar+userDollar(f,users,referrals,reward)
    return dollar
    
def userDollar(user,users,referrals,reward):
    dollar = 0
    for idx in range(len(users)):
        if user == users[idx]:
            if referrals[idx]!='':
                dollar=dollar+reward+userDollar(referrals[idx],users,referrals,reward/2)
    return dollar

