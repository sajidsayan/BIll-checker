a = 3492
print(f"Your bill is {a}$")
b = int(input("Give your bill: "))
if b > a:
    print("Thanks for your patience")
elif a == b:
    print("Thanks for your patience")
else:
    more = a-b
    print(f"You need to pay more {more}$")
