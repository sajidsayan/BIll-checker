a = 3492
print(f"Your bill is {a}$")
b = int(input("Give your bill: "))

if a == b:
    print("Thanks for your patience")
elif b > a:
    more2  = b - a
    print(f"You payed more than bill take your {more2}$ ")
else:
    more = a-b
    print(f"You need to pay more {more}$")
