import csv
with open('MovieGeeky/movies_data.csv', newline='') as csvfile:
    dict_reader = csv.DictReader(csvfile)

    #get header fieldnames from DictReader and store in list
    headers = dict_reader.fieldnames
    #print(headers)

    movies_data = list(list(row.values()) for row in dict_reader)
    #print(movies_data)
    """
    ---Same thing but used list comprehension above--
    movies_data = []
    for row in dict_reader:
        movies_data.append(list(row.values()))
    print(movies_data)
    """

    csvfile.seek(len(headers))
    #list with all the genres available in the movies data file
    movies_genres = list(dict.fromkeys(row['genres'] for row in dict_reader if row['genres'] != ''))
    #print(movies_genres)
    
    """
    ---Same thing but used list comprehension above--
    for row in dict_reader:
        if row['genres'] not in genres_list:
            genres_list.append(row['genres'])
        #print(row['genres'])
    """


    def print_details(movie):
        print("------------------------------")
        for details in movie:
            print(details)
        print("------------------------------")