def circle(radius):
    pi = 3.14159
    return pi * radius ** 2

def taxes(money, tax):
    return money + (money * tax / 100)

def temp(f):
    return (f - 32) * (5 / 9)

r = float(input("Enter radius: "))
print(f"{circle(r):.2f}")

m = float(input("Enter money: "))
t = float(input("Enter tax rate: "))
print(f"{taxes(m, t):.2f}")

f = float(input("Enter Fahrenheit: "))
print(temp(f))