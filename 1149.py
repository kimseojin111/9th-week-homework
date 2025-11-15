import sys 
lambda input : sys.stdin.readline   
'''
같은 dp 를 사용한다. 
dp[i][j] = min(dp[i-1][k]) (k!=j) + a[i][j]  
'''

n = int(input()) 
a = [[0]*3 for _ in range(n)] 
dp = [[0]*3 for _ in range(n)] 

for i in range(n):
    inp = list(map(int,input().split()))
    for j in range(3):
        a[i][j] = inp[j] 
    for j in range(3):
        dp[i][j] = a[i][j] 
        if i==0: 
            continue 
        to_add = 10000000000000000000 
        for k in range(3):
            if k!=j: 
                to_add = min(to_add,dp[i-1][k]) 
        dp[i][j] += to_add 

print(min(dp[n-1]))