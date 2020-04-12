def knapSack(W , wt , val , n): 
    if n == 0 or W == 0 : 
        return 0
    if (wt[n-1] > W): 
        return knapSack(W , wt , val , n-1) 
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1), 
                   knapSack(W , wt , val , n-1)) 
  
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapSack(W , wt , val , n))

def lps(str): 
    n = len(str) 
    L = [[0 for x in range(n)] for x in range(n)] 
    for i in range(n): 
        L[i][i] = 1 
    for cl in range(2, n+1): 
        for i in range(n-cl+1): 
            j = i+cl-1
            if str[i] == str[j] and cl == 2: 
                L[i][j] = 2
            elif str[i] == str[j]: 
                L[i][j] = L[i+1][j-1] + 2
            else: 
                L[i][j] = max(L[i][j-1], L[i+1][j]); 
  
    return L[0][n-1] 
  
seq = "TESTING"
n = len(seq) 
print("The length of the LPS is " + str(lps(seq))) 
