def hows_the_parrot():
    print("He's pining for the fjords!")
    
hows_the_parrot()

def lumberjack(name):
    if name.lower() == 'kenneth':
        print ("Kenneth's a lumberjack and he's OK!")
    else:
        print("{} sleeps all night and {} works all day!".format(name, name))
        
lumberjack("Elaine")