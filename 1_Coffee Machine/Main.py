def coffeeMachine():
    
    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    changeInMachine = 0.0


    exit = False  #tells about the  exit scenario
    choices = 'espresso latte cappuccino'.split()
    

    while exit is False:
        print("What would you like?(espresso/latte/cappuccino):")
        choice = input().lower()

        

        if choice == 'off':
            exit = True
            break
        
        #if choice is report
        elif choice == 'report':

            for key , value in resources.items():
                print("{a} : {b}".format(a = key , b = value))

            print("Money : ${:.2f}".format(changeInMachine))
        
        
        #if choice is within the listed item
        elif choice in choices:

            enoughResources = True
            for key , value in  MENU[choice]['ingredients'].items():
                if resources[key] < value:
                    print("Sorry, there is not enough" ,key )
                    enoughResources = False
                    break


            #precessing coins    
            if enoughResources == True:

                coinValues = [0.25 , 0.10 , 0.05 , 0.01]
                coinNames = ["quarters" , " dimes" , "nickel" , "pennies"]
                totalAmountReceived = 0.0
                itemCost = MENU[choice]['cost']

                print("Please insert coins.")
                
                for i in range(len(coinValues)) :
                    print("How many {} ?: ".format(coinNames[i]))
                    totalAmountReceived += coinValues[i] * int(input())

                #checking if money submitted is equal or not
                if totalAmountReceived < itemCost:
                    print("Sorry that's not enough money. Money refunded.")
                elif totalAmountReceived >= itemCost:
                    
                    print("Here is the change : {:.2f}".format((totalAmountReceived - itemCost)))
                    changeInMachine += totalAmountReceived 

                    for key , value in  MENU[choice]['ingredients'].items():
                        resources[key] -= value

                    print("Here is your {}.Enjoy!".format(choice))

coffeeMachine()
























        

          
