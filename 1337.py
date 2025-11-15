import sys 
lambda input : sys.stdin.readline   
'''
5개의 연속 원소에 대해서 맨 첫 원소가 배열중 하나라 가정할 수 있다. 
'''

ans  = 5 
n = int(input()) 
arr = [] 
for i in range(n):
    arr.append(int(input())) 
# 중복 제거 
s = set(arr) 
for x in s: 
    tmp = 4 
    for chk in range(x+1,x+5):
        if chk in s: 
            tmp -= 1 
    ans = min(ans, tmp)

print(ans)
