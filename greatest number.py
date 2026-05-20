a = float(input("Greatest number is:2.45 "))
b = float(input("Greatest number is:1.5 "))
c = float(input("Greatest number is:3.2 "))

if (a >= b) and (a >= c):
    largest = a
elif (b >= a) and (b >= c):
    largest = b
else:
    largest = c

print(f"The greatest number is: {largest}")