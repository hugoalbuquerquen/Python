import csv
with open('movie_data_set.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        if "Action Dra" in row['genres']:
            print("{0} - {1} - {2}".format(row['title'], row['runtime'], row['director']))