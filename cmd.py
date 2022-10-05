import cmd_dict
#### file handling
### exe. before main to create a movie_lib []
## open movie.txt and reads contents
# appends into movie_lib(type: list)
FILE = "movies.txt"
def init_list():
    movie_lib = []
    with open(FILE) as file:
        for i in file:
            movie_lib.append(i)
    return movie_lib


## called by add_movie()
# writes contents of movie_lib to file
def file_write(movie):
    with open(FILE, 'a+') as file:
        file.write(f"{movie}\n")


## called by delete_movie()
def file_delete(movie):
    with open(FILE, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if line.strip('\n') != movie:
                file.write(line)
        file.truncate()


### main functions
## display menu
def display_menu():
    print(f"\nCommand Menu")
    print(f"list - list all movies")
    print(f"add - Add a movie")
    print(f"del - Delete a movie")
    print(f"exit - Exit program\n")


## data entry validation
def entry_validate():
    running = True
    while running:
        display_menu()
        try:
            entry = input(f"Command: ")
            valid_entry = entry.lower()
        except ValueError:
            print("Not a valid command. Please try again")
            continue
        if valid_entry not in cmd_dict.commands:
            print("Not a valid command. Please try again")
            continue
        if valid_entry is not None:
            running = False
    return valid_entry


### list handling functions
## cmd_dict maps to user_cmds
# function for displaying list
def list_movies(movie_lib):
    print()
    print(f"Movie Library")
    for x, movie in enumerate(movie_lib, start=1):
        print(f"{x}.{movie}")


## add cmd - add movie to library
## 'w' - movies.txt
def add_movie(movie_lib):
    movie = input("Name: ")
    movie_lib.append(movie)
    file_write(movie)
    print()
    print(f"{movie} was added.\n")

## del cmd - deletes a element in movie_lib
def delete_movie(movie_lib):
    while 1:
        try:
            i = int(input("Index number: "))  # index of movie_lib(- 1)
        except ValueError:
            print("Invalid index, try again")
            continue
        if i < 1 or i > len(movie_lib):
            print("Invalid Index.\n")
            continue
        else:
            movie = movie_lib.pop(i - 1)
            file_delete(movie)
            print(f"{movie} was deleted.\n")
            return 0
