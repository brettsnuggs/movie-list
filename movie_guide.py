## Brett Snuggs, CIS 261, Movie Guide Part 1
import cmd
import cmd_dict

def main():

    movie_lib = cmd.init_list()

    print(f"\nThe Movie List Program")

    running = True
    while running:

        user_cmd = cmd.entry_validate()

        ## list cmd
        if user_cmd == cmd_dict.commands[0]:
            cmd.list_movies(movie_lib)
            continue
        ## add cmd
        elif user_cmd == cmd_dict.commands[1]:
            cmd.add_movie(movie_lib)

        ## del cmd
        if user_cmd == cmd_dict.commands[2]:
            cmd.delete_movie(movie_lib)

        ## exit cmd
        if user_cmd == cmd_dict.commands[3]:
            print("exit")
            running = False


if __name__ == "__main__":
    main()