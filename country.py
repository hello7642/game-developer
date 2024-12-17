capitals={"China":"Beijing",
          "America":"Washington",
          "Germany":"Berlin",
          "India":"New Delhi",
          "South Korea":"Seoul"}
while True:
    print("What do you want to do?\n1.View Dictionary\n2.Add a country and capital\n3.print capital of a country\n4.Deleting country\n5.Exit")
    choice=int(input())
    if choice==1:
        print(capitals)
    elif choice==2:
        country=input("What country do you want to add?")
        cap=input("What capital do you want to add?")
        capitals[country]=cap
    elif choice==3:
        coun=input("Which country's capital do you want to print?")
        print(capitals.get(coun,"does not exist"))
    elif choice==4:
        d=input("Which country and capital do you want to delete?")
        del capitals[d]
    elif choice==5:
        print("Good bye")
        break
    
    
    
    
    