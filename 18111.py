import sys 
lambda input : sys.stdin.readline 

n,m,B = map(int,input().split()) 
arr = [] 
for i in range(n):
    inp = list(map(int,input().split())) 
    arr += inp 

ans_list = [] 
for h in range(0,257):
    inven = B 
    time_spent = 0 
    for x in arr:
        if x > h: 
            time_spent += 2*(x-h) 
            inven += x-h 
    
    block_needed = 0 
    for x in arr:
        if x<h: 
            time_spent += (h-x) 
            block_needed += h-x 
    
    if inven>=block_needed:
        ans_list.append((time_spent,h)) 

ans_list.sort(key=lambda x: (x[0],-x[1])) 
print(*ans_list[0])