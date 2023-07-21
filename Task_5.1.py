import csv

with open('Favorite_books.csv', 'w', newline='') as file:
    field_names = ["Book", "Author", "Year of release"]
    writer_book = csv.DictWriter(file, fieldnames=field_names)

    writer_book.writeheader()
    writer_book.writerow({"Book": "The Alchemist",
                          "Author": "Paulo Coelho",
                          "Year of release": "2021"})

    writer_book.writerow({"Book": "All adults are unhappy",
                          "Author": "Kara Lynn",
                          "Year of release": "2022"})

    writer_book.writerow({"Book": "Player's handbook",
                          "Author": "Jeremy Crawford",
                          "Year of release": "2021"})

    writer_book.writerow({"Book": "Captain Grant's Children",
                          "Author": "Jules Verne",
                          "Year of release": "2021"})

    writer_book.writerow({"Book": "Fullmetal Alchemist (01)",
                          "Author": "Hiromu Arakawa",
                          "Year of release": "2019"})

print("The csv-file has been created and is ready to work!")
