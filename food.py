order_dict = {
    "burger":45.00,
    "pizza":55.00,
    "dhosa":65.00,
    "biryani":75.00,
    "pepsi":30.00,
    "manchuriyan":99.00,
    "pulav":90.00,
    "tea":25.00,
    "sandwich":50.00,
    "ice-cream":30.00
}

def order_food():
    total_bill = 0
    print("\n")

    for food,price in order_dict.items():
        print("{:<15} : {:>3}".format(food.capitalize(), price))

    item_no = int(input("\nHow many food item want to add : "))

    while item_no>0:
        food_name = input("\nEnter Food Name : ")

        if food_name.lower() in order_dict:
            print(f"Your Order : {food_name.capitalize()} in {order_dict[food_name]}")
            total_bill+=order_dict[food_name]
            print(f"Bill : {total_bill}")
        else:
            while food_name.lower() not in order_dict:
                valid_name = input("Enter valid name : ")
                if valid_name.lower() in order_dict:
                    print(f"Your Order : {valid_name.capitalize()} in {order_dict[valid_name]}")
                    total_bill+=order_dict[valid_name]
                    print(f"Bill : {total_bill}")
                    break
        item_no-=1
    print(f"\n\tYour total bill : {total_bill}")

    while True:
        print("\nHow do you want to Pay:\n1. Debit\n2. Cash")
        bill_choice = int(input("Enter number that choose to pay : "))
        if bill_choice==1:
            debit_num = int(input("Enter Debit Card number : "))
            cash_num1 = int(input("Enter Cash that you Pay : ")) 
            debit_pin = int(input("Enter Pin number : "))
            total_bill -= cash_num1 
            if total_bill==0:
                print("Payment Successfull...")
                break
            else:
                print(f"This much money left : {total_bill}")
        elif bill_choice==2:
            cash_num = int(input("Enter Cash : "))
            total_bill -= cash_num
            if total_bill==0:
                print("Payment Successfull...")
                break
            else:
             print(f"This much money left : {total_bill}")
        else:
            print("Enter valid number...")

def admin_panle():
    while True:
        print("\nHey Admin what you want :")
        print("1. Add Food\n2. Delete Food\n3. Update Price\n4. Exit")
        admin_choice = int(input("\nEnter Choice : "))
        if admin_choice==1:
            add_food_num = int(input("How many food do you want to add : "))
            while add_food_num>0:
                food_name = input("Enter Food Name : ")
                food_price = float(input("Enter Food Price : "))
                order_dict.setdefault(food_name,food_price)
                print(f"{food_name} with ₹{food_price} add successfully...")
                add_food_num-=1
        elif admin_choice==2:
            print("\n")
            for food,price in order_dict.items():
                print("\t{:<15}:{:>3}".format(food,price))
            del_food_num = int(input("\nHow many food do you want to remove : "))
            while del_food_num>0:
                food_name = input("Enter Food Name : ")
                order_dict.pop(food_name)
                print(f"{food_name} remove successfully...")
                del_food_num-=1
        elif admin_choice==3:
            print("\n")
            for food,price in order_dict.items():
                print("\t{:<15}:{:>3}".format(food,price))
            update_price = int(input("How many food items price do ou want add : "))
            while update_price>0:
                food_name = input("Enter Food Name : ")
                if food_name in order_dict:
                    new_price = float(input("Enter new price : "))
                    if food_name in order_dict:
                        order_dict[food_name] = new_price
                        print(f"{new_price} add successfully...")
                update_price-=1
        elif admin_choice==4:
            print("Byy Admin..")
            break
        else:
            print("Enter valid number")
        
def food_main():
    print("\n\n\t\tWelcome to KhaooJiBharKe Resturent :)")
    while True:
        print("\n\n1. Order Food\n2. Admin Panle\n3. Want Exit\n")
        user_choice = int(input("\n\tEnter your choice : "))

        if user_choice==1:
            order_food()
        elif user_choice==2:
            admin_panle()
        elif user_choice==3:
            print("\t\nThanks For Comming... :)")
            break
        else:
            print("Wrong Number Choosed.. Try agin...")

if __name__ == "__main__":
    food_main()