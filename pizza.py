import time

toppingValue = [0,1,1.75,2.50,3.35]

print("Welcome to papa's playfully patriotic and painstakingly passionate pizza parlor")
time.sleep(2)
print("What size pizza are you looking for today? (L or XL)")
pizzaSize = str(input())
if pizzaSize != "L" and pizzaSize != "XL":
    print("Pizza must be either large or extra large! (please use capital letters)")
elif pizzaSize == "L":
    print("How many toppings do you want (0 - 4)")
    topping = int(input())
    if topping > 4 or topping < 0:
        print("Toppings must be within 0 and 4! (no decimals)")
    subTotal = 6 + toppingValue[topping]
    print("Subtotal is: $", subTotal)
    total = subTotal * 1.13
    roundedTotal = str(round(total,2))
    if len(roundedTotal) < 4:
        roundedTotal += "0"
    print("Total is: $", roundedTotal)
elif pizzaSize == "XL":
    print("How many toppings do you want (0 - 4)")
    topping = int(input())
    if topping > 4 or topping < 0:
        print("Toppings must be within 0 and 4! (no decimals)")
    subTotal = 10 + toppingValue[topping]
    print("Subtotal is: $", subTotal)
    total = subTotal * 1.13
    roundedTotal = str(round(total,2))
    if len(roundedTotal) < 4:
        roundedTotal += "0"
    print("Total is: $", roundedTotal)