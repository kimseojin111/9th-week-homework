import sys 
lambda input : sys.stdin.readline   
'''
재귀를 이용한다. 
'''

def recursive(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']
    stars = recursive(n//2)
    top = [' '*(n//2) + star + ' '*(n//2) for star in stars]
    pedestal = [star + ' ' + star for star in stars]
    return top + pedestal

n = int(input())
print('\n'.join(recursive(n)))