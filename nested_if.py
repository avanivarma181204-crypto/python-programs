college=input("came to college?:")
if college == "yes":
    block=input("came to block?:")
    if block =="yes":
        floor=input("came to floor?:")
        if floor == "yes":
            classs=input("came to class?:")
            if  classs == "yes":
                print("the student is in the class")
            else:
                print("The student is in the floor")
        else:
            print("The student is  in the block")
    else:
        print("The student is in the college")
else:
    print("The student is absent")