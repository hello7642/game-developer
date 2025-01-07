with open("Story.txt","w") as file:
    file.write("Today i went to school. ")


with open("Story.txt","a") as file:
    file.write("I like playing video games.")


with open("Story.txt","r") as file:
    print(file.read())
