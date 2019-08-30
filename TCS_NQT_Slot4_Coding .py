n=int(input("Enter the Value"))
x=0
y=0
c='R'
while(n):
    if c=='R':
        x=abs(x)+10
        y=abs(y)
        c='U'
        n-=1
        continue
    elif c=='U':
        y=(y+20)
        c='L'
        n-=1
        continue
    elif c=='L':
        x=-(x+10)
        c='D'
        n-=1
        continue
    else:
        y=-y
        c='R'
        n-=1
        continue
print(x, y)







