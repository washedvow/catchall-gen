import names, random 

def catchall(): 
    
    count = int(input('How many do you want generated? '))
    print()

    # EDIT THIS TO YOUR OWN CATCHALL 
    catchall = ''

    for i in range(count):
        print(str(random.randint(1, 999)) + str(names.get_first_name()) + str(names.get_last_name()) + str(random.randint(1, 999)) + str('@') + str(catchall))

    print()

catchall()