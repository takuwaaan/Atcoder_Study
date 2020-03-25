a=list(input())
b=list(input())
c=list(input())
x=a.pop(0)
while True:
    if x=="a":
        if not a:
            print("A")
            break
        x=a.pop(0)
    elif x=="b":
        if not b:
            print("B")
            break
        x=b.pop(0)
    else:
        if not c:
            print("C")
            break
        x=c.pop(0)