import os

from data import *
from linkedlist import LinkedList


os.system('cls' if os.name == 'nt' else 'clear')

print("---------------------------------------------------------------")
print("Welcome to The MovieGeeky.\n")
print("I've got quite the movie library and will happily recommend movies to you.\n")
print("---------------------------------------------------------------")

def insert_genre_data():
    movie_genre_list = LinkedList()
    for movie_g in movies_genres:
        movie_genre_list.insert_beginning(movie_g)
    return movie_genre_list


def insert_movie_data():
    movies_data_list = LinkedList()
    for movie_g in movies_genres:
        movie_sublist = LinkedList()
        for movie in movies_data:
            if movie[0] == movie_g:
                movie_sublist.insert_beginning(movie)
        movies_data_list.insert_beginning(movie_sublist)
    return movies_data_list


my_genres_list = insert_genre_data()
my_movies_list = insert_movie_data()

selected_movie_genre = ""

while len(selected_movie_genre) == 0:

    user_input = str(input("\nType in the genre or the first letters of a genre you'd like recommendations for: ")).lower()

    matching_genres = []
    genre_list_head = my_genres_list.get_head_node()
    
    print("")
    while genre_list_head is not None:

        if str(genre_list_head.get_value()).lower().startswith(user_input):
            matching_genres.append(genre_list_head.get_value())
            print(genre_list_head.get_value())
        genre_list_head = genre_list_head.get_next_node()

    if len(matching_genres) == 1:

        #print("\nThe only matching genre is " + matching_genres[0] + ".")
        select_type = str(input("\nWould you like to look at " + matching_genres[0] + " movies? Enter y - Yes or n - No: ")).lower()

        if select_type == "y":
            selected_genre = matching_genres[0]
            print("Selected Movie Genre: " + selected_genre + "\n")
            movie_list_head = my_movies_list.get_head_node()

            
            while movie_list_head.get_next_node() is not None:
                sublist_head = movie_list_head.get_value().get_head_node()

                if sublist_head.get_value()[0] == selected_genre:

                    while sublist_head.get_next_node() is not None:
                        print("----------------------------------")
                        print(sublist_head.get_value()[1])
                        print(sublist_head.get_value()[2])
                        print(sublist_head.get_value()[3] + " min")
                        print(sublist_head.get_value()[4] + " / 10 IMDB")
                        print("By " + sublist_head.get_value()[5])
                        
                        sublist_head = sublist_head.get_next_node()

                movie_list_head = movie_list_head.get_next_node()
        
        print("----------------------------------")
        repeat_input = str(input("\nWould you like to look for a different genre? Enter y - Yes or n - No: ")).lower()
        if repeat_input == "y":
            pass
        else:
            print("\nThank you for visiting MovieGeeky, enjoy your movie.\n\n")
            break
    
    elif len(matching_genres) > 1:
        print("\nSorry, I've more than one option, please give me a few more letters.")

    else:
        print("Sorry, I've no movies genre with '" + user_input + "'. Please try again.")

    """

    print("")
    for movie in movies_data:
        if text in movie[0].lower():
            print("-----------------------------------------------------")
            for details in movie[1:]:
                if details == movie[3]:
                    print(details + " min")
                
                elif details == movie[4]:
                    print(details + " / 10")
                
                else:
                    print(details)
    """