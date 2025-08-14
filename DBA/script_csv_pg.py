import csv
import random

my_list = []
count = 0

def printAuthor(myList):
  for i in my_list:
    if len(i) > 1:
      #('first_name', 'last_name'),
      if len(i) == 3:
        print("('{} {}', '{}'),".format(i[0].strip(), i[1].strip(), i[2].strip()))
      else:
        print("('{}', '{}'),".format(i[0].strip(),i[1].strip()))

def printPublisher(myList):
  for i in my_list:
    #('pb_name', 'country'),
    print("{}('{}', NULL),".format(my_list.index(i),i))

def printBooks():
    # title = row['title'].replace("'","''").strip()
    # genres = row['genres'][1:-1].replace("'", "")
    # language = row['language'].replace(";", ",")
    # pb_name = row['publisher'].replace("'","''")
    # quantity = random.randrange(2,5)

    # if isbn not in my_list and pb_name != "":
    #   my_list.append(isbn)

    #   print("('{}', '{}', '{}', '{}', '{}', {}),".
    #     format(isbn, title, genres, language, pb_name, quantity))
  return 0

with open("./books_library.csv", encoding="utf8") as library_file:
  library_reader = list(csv.DictReader(library_file))

with open("./data-authors.csv", encoding="utf8") as authors_file:
  author_reader = csv.DictReader(authors_file)

  for author_row in author_reader:
    #print(author_row['id'], "{} {}".format(author_row['first_name'],author_row['last_name']))

    author_pg = "{} {}".format(author_row['first_name'],author_row['last_name'])

    #print(author_pg)

    for lib_row in library_reader:
      count += 1

      isbn = lib_row['isbn']
      pb_name = lib_row['publisher'].replace("'","''")
      authors = lib_row['authors']

      if authors == author_pg and isbn not in my_list:
        my_list.append(isbn)
        print("('{}', {}),".format(isbn, author_row['id']))
        #print(isbn, author_row['id'],author_pg)
    

  #('isbn', 'id_author') Erin Morgenstern