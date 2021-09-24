
choices =int(input())
t = int(input("place your temp value"))

def choice():
    if choices == 1:
        print((t*9/5)+32,"the temperature change from celsius to fahrenheit")
    
    elif choices >= 3:
        print("try again")
    else:
        print((t - 32) * 5/9, "the temperature change from fahrenheit to celsius")
choice()


#this code will change temperature from celsius to fahrenheit


#def changetemp():
    #print((t*9/5)+32)

#changetemp()

