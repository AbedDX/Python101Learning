#Kirjasto:
#Luodaan Kirjasto. Meillä on Book ja Library luokat. Book sisältää numeraalisen id:n, 
#kirjan nimen, kirjailijan nimen, sivumäärän, genren ja onko kirja lainassa. 
#Aluksi Libraryyn tehdään __init__ funktiossa lista, johon lisätään vähintään viisi kirjaa.
#Lisätään funktiot kirjan lainaamiselle ja palauttamiselle id:n avulla. 
#Lisäks funktiot listaamaan kirjat erotellen lainassa olevat muista kirjoista.
#Mainissa pyöritetään while loopissa kyselyä, että mitä käyttäjä haluaa tehdä kunnes q eli quit.
# Bonus: Lisää kirjojen lisääminen Libraryyn. 


class Library:
    def __init__(self):
        self.books = []
        self.checked_out_books = {}
        self.load_books_from_file()

    def load_books_from_file(self):
        try:
            with open("library_books.txt", "r") as file:
                lines = file.readlines()
                self.books = []
                self.checked_out_books = {}
                for line in lines:
                    book_data = line.strip().split(',')
                    book_id, title, author, checked_out = map(str.strip, book_data)
                    book = {'id': int(book_id), 'title': title, 'author': author}
                    if checked_out == 'True':
                        self.checked_out_books[int(book_id)] = book
                    self.books.append(book)
        except FileNotFoundError:
            pass

    def save_books_to_file(self):
        with open("library_books.txt", "w") as file:
            for book in self.books:
                book_id = book['id']
                title = book['title']
                author = book['author']
                checked_out = 'True' if book_id in self.checked_out_books else 'False'
                file.write(f"{book_id},{title},{author},{checked_out}\n")

    def add_book(self, title, author):
        book_id = len(self.books) + 1
        book = {'id': book_id, 'title': title, 'author': author}
        self.books.append(book)
        self.save_books_to_file()
        print(f"{title} lisättiin kirjastoon.")

    def list_books(self):
        print("\nKirjastossa olevat kirjat:")
        for book in self.books:
            if book['id'] in self.checked_out_books:
                print(f"{book['id']}: {book['title']} ({book['author']}) - Lainassa")
            else:
                print(f"{book['id']}: {book['title']} ({book['author']})")

    def borrow_book(self, book_id):
        if book_id in self.checked_out_books:
            print("Tämä kirja on jo lainassa.")
        else:
            for book in self.books:
                if book['id'] == book_id:
                    self.checked_out_books[book_id] = book
                    self.save_books_to_file()
                    print(f"{book['title']} on nyt lainassa.")

    def return_book(self, book_id):
        if book_id in self.checked_out_books:
            book = self.checked_out_books.pop(book_id)
            self.save_books_to_file()
            print(f"{book['title']} palautettiin onnistuneesti.")
        else:
            print("Tämä kirja ei ole lainassa.")

def main():
    library = Library()
    
    while True:
        print("\nValitse toiminto:")
        print("1. Lisää kirja")
        print("2. Listaa kirjat")
        print("3. Lainaa kirja")
        print("4. Palauta kirja")
        print("q. Poistu")
        
        choice = input("Valintasi: ")
        
        if choice == '1':
            title = input("Syötä kirjan nimi: ")
            author = input("Syötä kirjan kirjailija: ")
            library.add_book(title, author)
        elif choice == '2':
            library.list_books()
        elif choice == '3':
            book_id = int(input("Syötä kirjan ID, jonka haluat lainata: "))
            library.borrow_book(book_id)
        elif choice == '4':
            book_id = int(input("Syötä kirjan ID, jonka haluat palauttaa: "))
            library.return_book(book_id)
        elif choice == 'q':
            print("Kiitos käynnistä! Hei hei.")
            break
        else:
            print("Virheellinen valinta. Yritä uudelleen.")

if __name__ == "__main__":
    main()


