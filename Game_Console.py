from Calculator import calculator
from Hangman import hangman
from Guess_the_number import guess_the_number


def main():
    print("აირჩიეთ სასურველი ფუნქცია:")
    print("1. კალკულატორი")
    print("2. Hangman თამაში")
    print("3. ციფრის გამოცნობა")

    
    choice = input("აირჩიეთ სასურველი ფუნქციის შესაბამისი ციფრი: ")
    
    if choice == '1':
        calculator()
    elif choice == '2':
        hangman()
    elif choice == '3':
        guess_the_number()

    else:
        print("არასწორი არჩევანი. გთხოვთ, სცადეთ თავიდან.")

if __name__ == "__main__":
    main()