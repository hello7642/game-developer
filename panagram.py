import string
alphabet=set(string.ascii_lowercase)
sen=input("Please enter a sentence:")
senset=set(sen.lower())
print(senset)
is_panagram=True
for i in alphabet:
    if i not in senset:
        is_panagram=False
        break
if is_panagram:
    print("The sentence you typed is a panagram.")
else:
    print("The sentence you have typed is not a panagram.")

