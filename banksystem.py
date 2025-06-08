import random 
import math

file = open("bank.txt","w")

def create_Account():
    name = input("Enter Account Holder Name : ")
    address = input("Enter Account Holder Address : ")
    city = input("Enter Account Holder City Name : ")
    phone = input("Enter Account Holder Phone Number : ")
    account_number = random.uniform(100000,999999)

    if phone>=10:
        print("Phone number must be 10 digits.")
    else:
        print(f"Your Account Number : {math.floor(account_number)}")
        print("your account create successfully...")

    
    #file.write(account_number,"\n",name,"\n",address,"\n",city,"\n",phone)
    
    print("here your data :")
    print(f"Name : {name}\nAddress : {address}\nCity : {city}\nPhone : {phone}")



def bank_system():
    print("\n\n\t\tWelcome to Apna bank.\n")
    while(True):
        print("1.Create Account\n2.View Account By Search\n3.View All Account\n4.Delete Account\n5.Deposit\n6.Withdraw\n7.Exit\n")
        option = int(input("Enter your chocie : "))
        if option == 1:
            create_Account()
        elif option == 2:
            print("search account")
        elif option == 3:
            print("search account")
        elif option == 4:
            print("search account")
        elif option == 5:
            print("search account")
        elif option == 6:
            print("search account")
        elif option == 7:
            print("Thanks for comming...")
            break
        else:
            print("Error : enter valid number!")



bank_system()