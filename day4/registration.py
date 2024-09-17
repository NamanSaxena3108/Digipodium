print("Registration Application")
username=input("enter your name =>")
email=input("enter your email =>")
password=input("enter your password =>")
cpassword=input("enter your confirm password =>")
if username and email and password and cpassword:
    if username.isalnum():
        if '@' in email and email.endswith('.com'):
            if password == cpassword:
                if len(password)>=0:
                    print("Registration Complete 🎉🎉🎉🎉")
                else:
                    print("password too small")
            else:
                print("Password does not match")
        else:
            print("email is invalid")
    else:
        print("user name invalid")
else:
    print("Kindly fill the form correctly with all details")