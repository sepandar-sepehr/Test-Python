import math
Probs = {}
ProbsHeads = {}

def coinFlipSeq(length,p,groupsNo):
	if groupsNo < 1:
		return 0.0
	elif length > 0:
		answer = 0.000
		for gNo in range(groupsNo,length+1):
			seq1 = p*coinFlipSeq2(length,'h', p, gNo)
			seq2 = (1-p)*coinFlipSeq2(length,'t', p, gNo)
			answer +=  seq1 + seq2
		return round(answer,8)
	else:
		return 0.0
		
def coinFlipSeq2(length,first,p,groupsNo):
	if (length,first,groupsNo) in Probs:
		return Probs[(length,first,groupsNo)]
	if length < groupsNo:
		return 0.0
	elif length == 1:
		if groupsNo == 1:
			return 1.0
		else:
			return 0.0
	elif first == 'h':
		seq1 = p*coinFlipSeq2(length-1,'h',p,groupsNo)
		seq2 = (1-p)*coinFlipSeq2(length-1,'t',p,groupsNo-1)
		Probs [(length,first,groupsNo)] = seq1+seq2
		return seq1 + seq2
	else:
		seq1 = p*coinFlipSeq2(length-1,'h',p,groupsNo-1)
		seq2 = (1-p)*coinFlipSeq2(length-1,'t',p,groupsNo)
		Probs [(length,first,groupsNo)] = seq1+seq2
		return seq1 + seq2

def coinFlipSeqMoreHeads(length,p,groupsNo,headsNo):
	sumP = 0.000
	for i in range(headsNo, length+1):
		sumP += coinFlipSeqHeads(length,p,groupsNo,i)
	return sumP

def coinFlipSeqHeads(length,p,groupsNo,headsNo):
	if groupsNo < 1:
		return 0.0
	elif length > 0:
		answer = 0.000
		for gNo in range(groupsNo,length+1):
			seq1 = p*coinFlipSeqHeads2(length,'h', p, gNo, headsNo-1)
			seq2 = (1-p)*coinFlipSeqHeads2(length,'t', p, gNo, headsNo)
			answer +=  seq1 + seq2
		return round(answer,8)
	else:
		return 0.0
		
def coinFlipSeqHeads2(length,first,p,groupsNo,headsNo):
	if (length,first,groupsNo,headsNo) in ProbsHeads:
		return ProbsHeads[(length,first,groupsNo,headsNo)]
	if length < groupsNo:
		return 0.0
	elif length == 1:
		if groupsNo == 1 and headsNo <= 0:
			return 1.0
		else:
			return 0.0
	elif first == 'h':
		seq1 = p*coinFlipSeqHeads2(length-1,'h',p,groupsNo,headsNo-1)
		seq2 = (1-p)*coinFlipSeqHeads2(length-1,'t',p,groupsNo-1,headsNo)
		ProbsHeads [(length,first,groupsNo,headsNo)] = seq1+seq2
		return seq1 + seq2
	else:
		seq1 = p*coinFlipSeqHeads2(length-1,'h',p,groupsNo-1,headsNo-1)
		seq2 = (1-p)*coinFlipSeqHeads2(length-1,'t',p,groupsNo,headsNo)
		ProbsHeads [(length,first,groupsNo,headsNo)] = seq1+seq2
		return seq1 + seq2
		
def nMoreHeads(length, p, headsNo):
	sumP = 0.000
	for i in range(headsNo, length+1):
		x = math.factorial(length)/(math.factorial(i)*math.factorial(length-i))
		sumP += x * math.pow(p,i)*math.pow(1-p,length-i)
	return sumP

print(coinFlipSeq(2,.6,1))
print(coinFlipSeq(2,.6,2))
print(coinFlipSeq(3,.6,2))
print(coinFlipSeq(4,.6,2))
print "Q2.1: "+ str(coinFlipSeq(10,.6,6))
print "Q2.2: "+ str(round(coinFlipSeq(10,.6,6)/coinFlipSeq(10,.6,5),8))
print "Q2.3: "+ str(round(coinFlipSeqMoreHeads(10,.6,6,6)/nMoreHeads(10,.6,6),8))
print "Q2.4: "+ str(coinFlipSeq(100,.6,55))
print "Q2.5: "+ str(round(coinFlipSeqMoreHeads(100,.6,55,60)/nMoreHeads(100,.6,60),8))