
def comp():
    l=[]
    for i in range(2):
        gn=input("Enter group name:")
        gs=input("Enter group size:")
        dc=input("Enter date of competition")
        v=input("Enter venue")
        tm=input("Enter type of medal:")
        t=(gn,gs,dc,v,tm)
        l.append(t)
    return l


details=comp()
for i in details:
    print(i)























