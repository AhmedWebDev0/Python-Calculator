a = input("write :")

def clean_world (world):

    if len(world) == 1 :

        return world
        
    if world[0] == world[1] : 

        return clean_world (world[1:])
    
    return world[0] + clean_world (world[1:]) 

print(clean_world (a))

        
