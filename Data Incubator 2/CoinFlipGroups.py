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
		
def coinFlipSeq2(length,prev,p,groupsNo):
	if length < groupsNo:
		return 0.0
	elif length == 1:
		if groupsNo == 1:
			return 1.0
		else:
			return 0.0
	elif prev == 'h':
		seq1 = p*coinFlipSeq2(length-1,'h',p,groupsNo)
		seq2 = (1-p)*coinFlipSeq2(length-1,'t',p,groupsNo-1)
		return seq1 + seq2
	else:
		seq1 = p*coinFlipSeq2(length-1,'h',p,groupsNo-1)
		seq2 = (1-p)*coinFlipSeq2(length-1,'t',p,groupsNo)
		return seq1 + seq2
		

print(coinFlipSeq(10,.6,6))
print(coinFlipSeq(10,.6,5))
print round(coinFlipSeq(10,.6,6)/coinFlipSeq(10,.6,5),8)
print(coinFlipSeq(100,.6,55))