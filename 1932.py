import sys 
lambda input : sys.stdin.readline  
'''
dp[i][j] = i,j 까지 도달하는데 최대로 합쳐진 값으로 정의하자. 
dp[i][j] = max(dp[i+1][j],dp[i++1][j+1]) + a[i][j] 임을 알 수 있다. 
'''

n = int(input()) 
a = [[0]*n for _ in range(n)] 
for i in range(n):
    inp = list(map(int,input().split())) # '2 4 5' -> [2,4,5] 
    for j in range(i+1): 
        a[i][j] = inp[j] 
dp = [[0]*n for _ in range(n)] 
for i in range(n): 
    dp[n-1][i] = a[n-1][i] 

for i in range(n-2,-1,-1):
    for j in range(i+1):
        dp[i][j] = max(dp[i+1][j],dp[i+1][j+1]) + a[i][j] 
    
print(dp[0][0])