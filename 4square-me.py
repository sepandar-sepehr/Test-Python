def FSFD():
	for a in range(0,10):
		for b in range(0,a+1):
			for c in range(0,b+1):
				for d in range (0,c+1):
					if (a*a + b*b + c*c + d*d) % 59 == 7:
                        print "%d%d%d%d" %(a,b,c,d)
