d={"monday":"playing minecraft",
   "tuesday":"playing roblox",
  "wednesday":"play football",
  "thursday":"play fortnite",
  "friday":"watch tv"}
print(d["thursday"])
print(d.keys())
print(d.values())
for i in d.keys():
    print(i,d[i])

for i,j in d.items():
    print(i,j)

d["saturday"]="play badminton"
print(d)

del(d["monday"])
print(d)

d["sunday"]=["eat","party","sleep"]
print(d)
print(d["sunday"][1])

#nested dictionary
classroom={"Aakash":{"age":11,"marks":[91,87,75,99,85,77]},
           "Thomas":{"age":11,"marks":[65,86,78,68,97,54,60]},
            "George":{"age":11,"marks":[74,67,90,79,98,68,75]}}
print(classroom.keys())
print(classroom["George"]["marks"])
print(classroom["Aakash"]["age"])
print(classroom["Thomas"]["marks"][6])
print(classroom.get("Tyler"))

print(len(d))

print("monday"in d)

