x=int(input("enter marks:"))
if x >90:
    print("A grade")
elif x > 80 and x < 90:
    print("B grade")
elif x > 70 and x < 80:
    print("C grade")
elif x > 50:
    print("D grade")
elif x < 50 and x > 28:
    print("E grade")
else:
    print("fail")