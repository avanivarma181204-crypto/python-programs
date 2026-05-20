def Add(*args):
    print(*args)
    return sum(args)

print(Add(10,20))
result=Add(30,1)
print(result)