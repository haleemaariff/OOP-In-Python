#shooping cart program

foods= []
prices=[]
total= 0

while True:
    food = input("Enter the food to buy(q to quit):")
    if food.lower() =="q":
       break
    else:
        price=float(input("Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
print("-----Your Cart-----")        
for food in foods:
    print(food)
  #to print in one line
"""  print(food,end =" ")"""
for price in prices:
    total += price
print()
print(f"your total is :${total}")
