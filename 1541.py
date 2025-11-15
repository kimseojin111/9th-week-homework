import sys 
lambda input : sys.stdin.readline 
'''
풀이 설명: 
최대한 많이 뺴는 것이 이득이다. 
처음 - 가 나온 시점부터 모두 빼주는 것이 가능하다. 
ex) 50+20-10+30-20+40-10 -> 50+20-(10+30)-(20+40)-10 
'-' 기준으로 나눠주고 첫번째 이후로 모두 빼주도록 하자. 
'''

exp = input()
seq = exp.split('-') 

def f(inp):
    # '50+40+20' -> 110 
    nums = map(int,inp.split('+')) 
    # '50', '40', '20'   
    return sum(nums) 

a = list(map(f,seq)) 
ans = a[0] 
for i in range(1,len(a)):
    ans -= a[i] 
print(ans)