# 2.2 თამაში 1: გამოიცანით რიცხვი
# ამ თამაშში პროგრამა აგენერირებს შემთხვევით რიცხვს მითითებული დიაპაზონიდან.
#  მომხმარებლებს სთხოვენ გამოიცნონ რიცხვი. არასწორი რიცხვის შემთხვევაში პროგრამა მომხმარებელს აძლევს მინიშნებას
#  (უფრო მაღალი/უფრო დაბალი). თამაში აკონტროლებს მცდელობების რაოდენობას და აჩვენებს შედეგს, როდესაც მომხმარებელი გამოიცნობს სწორ რიცხვს.


import random

# ფუნქცია მინიშნებების მისაღებად
# აჩვენებს რამდენად ახლოს ხართ პასუხთან
def get_hint(guess, secret_number):
    difference = abs(guess - secret_number)
    
    if difference <= 5:
        return " ძალიან ახლოს ხართ!"
    elif difference <= 10:
        return " ცხელა!"
    elif difference <= 20:
        return " თბილა"
    elif difference <= 50:
        return " ცივა"
    else:
        return " ძალიან ცივა!"

# მთავარი თამაშის ფუნქცია
def guess_the_number():

    
    print(" კეთილი იყოს თქვენი მობრძანება რიცხვის გამოცნობის თამაშში!")
    
    while True:
        # თამაშის დაწყება
        lower_bound = 1
        upper_bound = 100
        secret_number = random.randint(lower_bound, upper_bound)
        attempts = 0

        print("\n" + "=" * 50)
        print(f"  გამოიცანით რიცხვი {lower_bound} და {upper_bound} შორის.")
        print("=" * 50)

        while True:
            try:
                # მომხმარებელს სთხოვს რიცხვის შეყვანას
                guess = int(input("\n შეიყვანეთ თქვენი ვარაუდი: "))
                attempts += 1

                # ვამოწმებთ პასუხს და ვაძლევთ მინიშნებებს
                if guess < secret_number:
                    print("⬆ მეტი რიცხვი სცადეთ.")
                    print(get_hint(guess, secret_number))  # ვაჩვენებთ მინიშნებას
                elif guess > secret_number:
                    print("⬇ ნაკლები რიცხვი სცადეთ.")
                    print(get_hint(guess, secret_number))  # ვაჩვენებთ მინიშნებას
                else:
                    # გამოიცანით!
                    print("\n" + "=" * 50)
                    print(f" გილოცავთ! გამოიცანით რიცხვი {secret_number}!")
                    print(f" დაგჭირდათ {attempts} მცდელობა")
                    
                    
                    print("=" * 50)
                    break
            except ValueError:
                print(" გთხოვთ შეიყვანოთ ვალიდური მთელი რიცხვი.")
        

        # ვკითხულობთ გსურთ თუ არა თავიდან თამაში
        play_again = input("\n გსურთ თავიდან თამაში? (დიახ/არა): ").lower()
        if play_again in ['არა', 'ara', 'no', 'n']:
            print("    გმადლობთ თამაშისთვის!")
            break


if __name__ == "__main__":
    guess_the_number()
