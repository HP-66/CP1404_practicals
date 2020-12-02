num=int(input("Number of items: "))
total=0
for i in range(num):
    price=float(input("Price of item: "))
    total=total+price
if total>100:
    total=total*0.9
print("Total price for",num,"items is ${:.2f}".format(total))
