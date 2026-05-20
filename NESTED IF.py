l_user="Avani Varma"
l_pass="181204"
username=input("enter username:")
if username==l_user :
    password=int(input("enter password:"))
    if password==l_pass:
        print("login successfull")
    else:
        print("wrong password")
else:
    print("wrong username")