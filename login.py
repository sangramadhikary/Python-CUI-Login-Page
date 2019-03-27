name=input("Enter Your Full Name: ")
txt=name+'.temp'

def login():
    global usernameE                         #Global Value Can Be Access On Any Functions
    global passwordE

    print('**********\nLOGIN\n******\nMr.',name)
    usernameE=input('Enter Your Username: ')          #Login Field For User Input
    passwordE=input('Enter Password: ')
    checklogin()

def signup():
    print('***************\nSIGNUP\n***********\nMr.',name)
    username=input("Enter Your Username: ")                #Signup Field For User Input
    password=input("Enter Password: ")
    
    with open(txt,'w') as n:
        n.write(username)                   #Creat A .Temp FIle To Store Signup Data
        n.write('\n')
        n.write(password)
        n.close()      
    login()

def checklogin():
    with open(txt,'r+') as n:
        data=n.readlines()                     #To Open & Read The .temp File      
        uname=data[0].rstrip()
        pword=data[1].rstrip()
    if usernameE==uname and passwordE==pword:           #Compare Either The Login Data Match With.temp Data Or Not
        print("You Have Sucsesfully Logedin")
    else:
        print("Access Denied")

check=int(input("\n1.If You Don't Have Account Signup\n2.If You Already Have Account Login\nEnter Here: "))
if check==1:
    signup()                                    #Ask User To Chose Signup Or Login
elif check==2:
    login() 
   