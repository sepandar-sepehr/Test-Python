def Four_Squares(N):
      M = [[] for T in range(N+1)]
         ## Element T of M will be populated with all pairs [a,b] such that a, b < sqrt(N) and a*a + b*b = T
         
      for a in range(0,int(sqrt(N//2)) + 1):
         for b in range(a,int(sqrt(N)) + 1):
            T = a*a + b*b
            if T <= N:
               M[T].append([a,b])
            else:
               break
 
      P = []
         ## P will be populated with all lists [a,b,c,d] such that 0 <= a <= b <= c <= d whose squares sum to N
 
      for i in range(0,N//2 + 1):
         if len(M[N-i]) == 0:
            break
         for j in range(0,len(M[i])):
            for k in range(0,len(M[N-i])):
               X = [M[i][j][0], M[i][j][1],
                    M[N-i][k][0], M[N-i][k][1]]
               if X[1] <= X[2]:
                  P.append(X)
 
      return P
