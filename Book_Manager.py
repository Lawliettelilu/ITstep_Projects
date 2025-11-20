# საჭირო მოდულის იმპორტი

import os


class Book:
    def __init__(self, title, author, year):
        # ინკაფსულაცია – ატრიბუტები ინახება ობიექტში
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"სათაური: {self.title}, ავტორი: {self.author}, წელი: {self.year}"



# 2. BOOKMANAGER კლასი – წიგნების მართვა

class BookManager:
    def __init__(self, filename="my_library.txt"):
        self.books = []              
        self.filename = filename     
        self.load_from_file()        # პროგრამის გაშვებისას გადმოიტვირთოს წიგნები ფაილიდან


    # წიგნის დამატება

    def add_book(self, book):
        self.books.append(book)
        print("\n წიგნი წარმატებით დაემატა!\n")
        self.save_to_file()


    # ყველა წიგნის ჩვენება

    def display_books(self):
        if not self.books:
            print("\nბიბლიოთეკაში წიგნები ჯერ არ არის.\n")
            return

        print("\n წიგნების სია ")
        for book in self.books:  
            print(book)
        print()


    # ძიება სათაურით

    def search_by_title(self, title):
        results = []
        for book in self.books:
            if book.title.lower() == title.lower():  
                results.append(book)
        return results

 
    # ფაილში შენახვა 

    def save_to_file(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            for book in self.books:
                line = f"{book.title}|{book.author}|{book.year}\n"
                file.write(line)


    # ფაილიდან წაკითხვა 

    def load_from_file(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    title, author, year = parts
                    self.books.append(Book(title, author, year))



# 3. დამხმარე ფუნქცია – წელზე ვალიდაცია

def get_valid_year():
    while True:
        year = input("შეიყვანეთ გამოცემის წელი: ")
        if year.isdigit():  # ვალიდაცია
            return int(year)
        print(" არასწორი წელი! შეიყვანეთ რიცხვი.")



# 4. მთავარი მენიუ და პროგრამის გაშვება

def main():
    manager = BookManager()

    while True:
        print("\n===== წიგნების მართვის მენიუ =====")
        print("1. წიგნის დამატება")
        print("2. ყველა წიგნის ნახვა")
        print("3. ძიება სათაურით")
        print("4. ფაილის წაშლა")
        print("5. გამოსვლა")

        choice = input("აირჩიეთ მოქმედება (1-5): ")

        if choice == "1":
            title = input("შეიყვანეთ სათაური: ").strip()
            author = input("შეიყვანეთ ავტორი: ").strip()
            year = get_valid_year()

            new_book = Book(title, author, year)
            manager.add_book(new_book)

        elif choice == "2":
            manager.display_books()

        elif choice == "3":
            title = input("სათაური: ")
            results = manager.search_by_title(title)

            if results:
                print("\nნაპოვნი წიგნები:")
                for book in results:
                    print(book)
            else:
                print("\n ასეთი წიგნი ვერ მოიძებნა.\n")

        elif choice == "4":
            manager.delete_file()

        elif choice == "5":
            print("გმადლობთ პროგრამის გამოყენებისთვის!")
            break

        else:
            print("არასწორი არჩევანი, სცადეთ თავიდან.")



# პროგრამის გაშვება

if __name__ == "__main__":
    main()
