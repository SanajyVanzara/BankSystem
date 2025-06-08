import random
from food import order_food
movie_list = {
    'Chaava' : 250,
    'Race 4' : 210,
    'Leo' : 150,
    'Hum Do Humare Do' : 110,
    'Sikandar' : 230,
    'Avtar 3' : 240,
    'Phir Hera Pheri 3' : 250,
    'Sky' : 160,
    'Dabang' : 200,
    'Pushpa 2' : 225,
}
book_movie = []
time_list = ["01:30","01:00","3:00","4:30","6:30","11:45","08:10","12:05","07:00","05:20","09:40"]
time_ampm = [" AM"," PM"]

def show_movie_list():
    print("\nMovie List :-----------------")
    for key, value in movie_list.items():
        print("{:<20}:{:>5}".format(key,value))
    print("-----------------------------\n")

def book_ticket():
    movie_name = input("Enter Movie Name : ")
    for i in movie_list.values():
        time_random = random.choice(time_list)
        time_chocie = random.choice(time_ampm)
        time = time_random + time_chocie
        if movie_name.title() in movie_list.keys():
            print(f"Movie : {movie_name.title()} -> Price : {movie_list[movie_name.title()]}, -> Time : {time}")
            book = input(f"Do you want to book {movie_name.title()} : ")
            if book.lower() == 'yes':
                while True:
                    pay = int(input(f"Pay {movie_list[movie_name.title()]} : "))
                    if pay == int(movie_list[movie_name.title()]):
                        print(f"{movie_name.title()} Booked Successfully...")
                        book_movie.append(movie_name.title())
                        return
                    else:
                        print(f"Pay only {movie_list[movie_name.title()]}")
        else:
            print(f"{movie_name.title()} Not Available, sorry...")
            break

def book_movies():
    if not book_movie:
        print("No Movies Booked...")
    else:
        print("\nBooked Movies :-\n")
        print(book_movie)

def admin_panel():
    while True:
        print("\nHey Admin what you want :")
        print("1. Show Movie\n2. Add Movie\n3. Delete Movie\n4. Update Price\n5. Exit")
        admin_choice = int(input("\nEnter Choice : "))
        if admin_choice==1:
            for movie,price in movie_list.items():
                print("\t{:<20}:{:>5}".format(movie.title(),price))
        elif admin_choice==2:
            add_Movie_num = int(input("How many Movie do you want to add : "))
            while add_Movie_num>0:
                Movie_name = input("Enter Movie Name : ")
                Movie_price = int(input("Enter Movie Price : "))
                movie_list.setdefault(Movie_name.title(),Movie_price)
                print(f"{Movie_name.title()} with ₹{Movie_price} add successfully...")
                add_Movie_num-=1
        elif admin_choice==3:
            for movie,price in movie_list.items():
                print("\t{:<20}:{:>5}".format(movie.title(),price))
            del_Movie_num = int(input("\nHow many Movie do you want to remove : "))
            while del_Movie_num>0:
                del_movie_name = input("Enter Movie Name : ")
                movie_list.pop(del_movie_name.title())
                print(f"{del_movie_name.title()} remove successfully...")
                del_Movie_num-=1
        elif admin_choice==4:
            for movie,price in movie_list.items():
                print("\t{:<20}:{:>5}".format(movie,price))
            update_price = int(input("How many Movie items price do you want add : "))
            while update_price>0:
                movie_name = input("Enter Movie Name : ")
                if movie_name.title() in movie_list:
                    new_price = int(input("Enter new price : "))
                    if movie_name.title() in movie_list:
                        movie_list[movie_name.title()] = new_price
                        print(f"{new_price} add successfully...")
                update_price-=1
        elif admin_choice==5:
            print("\nByy Admin..")
            break
        else:
            print("\nEnter valid number\n")

def movie_main():
    print("\n\tWelcome to Movie.com")
    while True:
        print("\n1.Show Movie List\n2.Book Ticket\n3.Show Booked Movies\n4.Food Booking\n5.Admin Panel\n6.Exit")
        chocie = int(input("Enter your chocie : "))

        if chocie == 1:
            show_movie_list()
        elif chocie == 2:
            book_ticket()
        elif chocie == 3:
            book_movies()
        elif chocie == 4:
            order_food()
        elif chocie == 5:
            admin_panel()
        elif chocie == 6:
            print("Exit programm....")
            break
        else:
            print("Enter valid number...")

if __name__ == "__main__":
    movie_main()