def student_details(name, age, marks, place="vizag", *hobbies, **kwargs):
    print("Name:", name)
    print("Age:", age)
    print("Marks:", marks)
    print("Place:", place)

    print("Hobbies:")
    for hobby in hobbies:
        print(":", hobby)
    for key, value in kwargs.items():
        print(key + ":", value)

student_details(
    "Avani",
    21,
    96,
    "vizag",
    "sketching", "Dancing",
    phone="9876543210",
    course="Python full stack")
