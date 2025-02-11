t=(7,89,"chocolate","chocolate","ice cream")
print(type(t))

t1=(8,9,"car",89,"bike")
print(type(t1))

print(t)

#t[3]="grapes"
for i in t:
    print(i,end=" ")
print()
#concatenation
print(t1+t)
print(t1,t)

#deleting a tuple
del t
print(len(t1))

#packing and unpacking
address=(47,"hello avenue","bye city","sl16 8rq")
(dno,st,ct,pc)=address
print(ct)



