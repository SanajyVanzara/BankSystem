import json

def load_data():
    try:
        with open("youtube.txt","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, vid in enumerate(videos, start=1):
        print(f"{index}. Name : {vid['Name']}, Duration : {vid['Time']}.")
    print("*" * 70)

def add_video(videos):
    name = input("\nEnter Video Name : ")
    time = input("Enter Video Duration : ")
    videos.append({"Name" : name,"Time" : time})
    save_data(videos)

def update_video(videos):
    list_all_videos(videos)
    num = int(input("\nEnter Video Number : "))
    if 1 <= num >= len(videos):
        name = input("Update Video Name : ")
        time = input("Update Video Duration : ")
        videos[num-1] = {"Name" : name,"Time" : time}
        print("Video Update Successfully..")
    else:
        print("\nEnter Valid Video Number...")
    save_data(videos)

def delete_video(videos):
    list_all_videos(videos)
    num = int(input("Enter Video Number : "))
    if 1 <= num >= len(videos):
        del videos[num-1]
        print(f"{num} Video Delete Successfully...")
    else:
        print("\nEnter Valid Video Number...")
    save_data(videos)

def save_data(videos):
    with open("youtube.txt","w") as file:
        json.dump(videos, file)

def main():
    videos = load_data()
    while True:
        print("\nYouTube Manager App | Features :-")
        print("1. List All YouTube  Videos")
        print("2. Add YouTube Video")
        print("3. Update YouTube Video")
        print("4. Delete YouTube Video")
        print("5. Exit")

        choice = int(input("Enter Feature : "))

        match choice:
            case 1:
                list_all_videos(videos)
            case 2:
                add_video(videos)
            case 3:
                update_video(videos)
            case 4:
                delete_video(videos)
            case 5:
                print("\nThanks For Using YouTube App...")
                break
            case _:
                print("\nInvalid Feature...")

if __name__ == "__main__":
    main()