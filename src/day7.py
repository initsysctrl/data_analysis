"""
斐波拉契数列
"""

buff=[]
def equili(n:int)->int:
    if n==0 or n==1:
        return n
    else:
        x=equili(n-1)+equili(n-2)
       
        return x

result=equili(7)
print(result)