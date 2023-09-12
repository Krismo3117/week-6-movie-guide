# Andrew Torres CIS 261

def display_menu():
    print("\nMovie List Menu")
    print("1. Display all titles")
    print("2. Add a title")
    print("3. Delete a title")
    print("4. Exit")
def read_movie_list():
    try:
        with open("movies.txt", "r") as file:
            movie_list = file.read().splitlines()
    except FileNotFoundError:
        movie_list = []
    return movie_list
def display_titles(movie_list):
    print("\nMovie Titles:")
    for index, title in enumerate(movie_list, start=1):
        print(f"{index}. {title}")
def add_title(movie_list):
    new_title = input("\nEnter the title to add: ")
    movie_list.append(new_title)
    with open("movies.txt", "a") as file:
        file.write(new_title + "\n")
    display_titles(movie_list)
def delete_title(movie_list):
    display_titles(movie_list)
    try:
        choice = int(input("\nEnter the number of the title to delete: "))
        if 1 <= choice <= len(movie_list):
            deleted_title = movie_list.pop(choice - 1)
            with open("movies.txt", "w") as file:
                file.writelines('\n'.join(movie_list))
            print(f"'{deleted_title}' has been deleted.")
            display_titles(movie_list)
        else:
            print("Invalid number. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
movie_list = read_movie_list()
while True:
    display_menu()
    choice = input("Enter your choice: ")
    
    if choice == "1":
        display_titles(movie_list)
    elif choice == "2":
        add_title(movie_list)
    elif choice == "3":
        delete_title(movie_list)
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid command. Please select a valid option.")

