admins =["Ahmed" , "Mustafa" ,"Joury" , "Osama" ,"Ali"]

name = input("Please type your name ").capitalize().strip()

if name in admins :

    print(f"Hello {name} Welcom Back")

    option = input("Delete or Update Your name?").strip().capitalize()
    
    if  option == "Update" or option == "U" :
        
        newname = input("Your New Name , please").strip().capitalize()
    
        admins[admins.index(name)] = newname
        print("Name Updated")
        print(admins)


    elif option == "Delete" or option == "D" :

        name.remove(name)
        print("Deleted successfully.")
        print(admins)
          
    else :

        print("Wrong Optuon Choosed")
 

else :
     
    status = input("You Aren\'t Admins ,Add You y,n?")

    if status == "Yes" or status == "Y":
        
        print("add successfully.")
        admins.append(name)

    else :

       print("You have not been added.")
