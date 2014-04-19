def FSFD():
	for a in range(0,10):
		for b in range(0,a):
			for c in range(0,b):
				for d in range (0,c):
					if (a*a + b*b + c*c + d*d) % 59 == 7:
						print a, b, c, d