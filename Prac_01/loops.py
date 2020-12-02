for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=" ")
print()

for i in reversed(range(1, 21)):
    print(i, end=" ")
print()

stars=int(input("Number of stars: "))
while stars>0:
    stars=stars-1
    print("*",end="")
print()

stars=int(input("Number of stars: "))
for i in range(1,stars+1):
    print("*"*i)
print()
