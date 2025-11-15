import sys 
lambda input : sys.stdin.readline 

'''
관찰 : 정답이 되는 과정은 무조건 존재한다. -> 모든 높이를 0으로 맞추면 된다. 
정답이 될 높이는 0이상 256이하이다. -> 256 보다 크게 만드는 것은 불필요하다. 
정답이 될 높이를 h로 고정시키자. 그러면 먼저 h보다 큰 애들을 모두 h로 맞춰준다. 
이때 남은 인벤토리 내부 블록 개수로 h보다 작은 애들을 체워줄 수 있으면 된다. 
'''

n,m,B = map(int,input().split()) 
arr = [] 
for i in range(n):
    inp = list(map(int,input().split())) 
    arr += inp 

# 그냥 높이만 필요하니 모두 flatten 시켜놓는다. 

ans_list = [] # 필요한 시간, h 쌍들을 저장할 리스트 
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