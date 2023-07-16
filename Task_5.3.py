import csv

start_year = str(input("Enter from which year inclusive to start searching for books: "))
finish_year = str(input("Enter from which year inclusive to finish searching for books: "))

while finish_year <= start_year:
    print("The beginning of the search is less than the end of the search!")
    finish_year = int(input("Enter the end of the search again: "))

csv_search = csv.reader((open("Favorite_books.csv", "r")))
count = 0

for row in csv_search:
    if (start_year <= row[2]) and (finish_year >= row[2]):
        print(row)
        count += 1

if count == 0:
    print("There are no books with such a release year interval in the table!")
