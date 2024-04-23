import time
import math

toppingValue = [0,1,1.75,2.50,3.35]

while True:
    print("Welcome to Papa Jackson's pizza parlor")
    time.sleep(2)
    print("What size pizza are you looking for? (Large or Extra large)")
    pizzaSize = str(input())
    if pizzaSize != "L" and pizzaSize != "XL" and pizzaSize != "l" and pizzaSize != "Large" and pizzaSize != "large" and pizzaSize != "Xl" and pizzaSize != "xL" and pizzaSize != "xl" and pizzaSize != "Extra large" and pizzaSize != "extra large" and pizzaSize != "extra Large":
        print("Pizza must be either large or extra large")
    elif pizzaSize == "L" or pizzaSize == "l" or pizzaSize == "Large" or pizzaSize == "large":
        print("How many toppings do you want (0 - 4)")
        topping = int(input())
        if topping > 4 or topping < 0:
            print("Toppings must be within 0 and 4 (no decimals)")
            break
        subTotal = 6 + toppingValue[topping]
        print("Subtotal is: $", subTotal)
        total = subTotal * 1.13
        roundedTotal = str(round(total,2))
        if len(roundedTotal) < 4:
            roundedTotal += "0"
        print("Total is: $", roundedTotal)
        print("Would you like another pizza? (Y or N)")
        retry = input()
        if retry == "Y" or retry == "y":
            time.sleep(1)
        elif retry == "N" or retry == "n":
            break
        else:
            print("Answer must be either Y or N (please use capital letters)")
            break
    elif pizzaSize == "XL" or pizzaSize == "Xl" or pizzaSize == "xL" or pizzaSize == "xl" or pizzaSize == "Extra large" or pizzaSize == "extra large" or pizzaSize == "extra Large":
        print("How many toppings do you want (0 - 4)")
        topping = int(input())
        if topping > 4 or topping < 0:
            print("Toppings must be within 0 and 4! (no decimals)")
            break
        subTotal = 10 + toppingValue[topping]
        print("Subtotal is: $", subTotal)
        total = subTotal * 1.13
        roundedTotal = str(round(total,2))
        if len(roundedTotal) < 4:
            roundedTotal += "0"
        print("Total is: $", roundedTotal)
        print("Would you like another pizza? (Y or N)")
        retry = input()
        if retry == "Y" or retry == "y":
            time.sleep(1)
        elif retry == "N" or retry == "n":
            break
        else:
            print("Answer must be either Y or N (please use capital letters)")
            break