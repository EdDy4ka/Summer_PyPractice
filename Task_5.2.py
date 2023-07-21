import csv

question = int(input("Add the number of records: "))

with open('Favorite_books.csv', 'a', newline='') as file:
    field_names = ["Book", "Author", "Year of release"]
    writer_book = csv.DictWriter(file, fieldnames=field_names)

    for i in range(question):
        print("The book: (", i + 1, ") of (", question, ")")
        book_q = str(input("Title of the book: "))
        author_q = str(input("Author of the book: "))
        year_q = str(input("The year of the book's release: "))
        writer_book.writerow({"Book": book_q,
                              "Author": author_q,
                              "Year of release": year_q})

search_author = str(input("Enter the author you want to find: "))
csv_search = csv.reader((open("Favorite_books.csv", "r")))
count = 0

for row in csv_search:
    if search_author == row[1]:
        print(row)
        count += 1

if count == 0:
    print("The books of this author are not contained in this table!")
