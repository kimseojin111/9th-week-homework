import sys 
lambda input : sys.stdin.readline  

n,r,c = map(int,input().split()) 

def recursive(n,r,c):
    if n==0:
        return 0
    mid = 1<<n-1 
    sz = 1<<2*n-2
    ans = 0 
    if c>=mid:
        ans += sz 
        c -= mid 
    if r>=mid:
        ans += sz*2 
        r -= mid 
    return ans + recursive(n-1,r,c) 

print(recursive(n,r,c))