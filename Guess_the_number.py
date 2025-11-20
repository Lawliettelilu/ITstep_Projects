# 2.2 თამაში 1: გამოიცანით რიცხვი
# ამ თამაშში პროგრამა აგენერირებს შემთხვევით რიცხვს მითითებული დიაპაზონიდან.
#  მომხმარებლებს სთხოვენ გამოიცნონ რიცხვი. არასწორი რიცხვის შემთხვევაში პროგრამა მომხმარებელს აძლევს მინიშნებას
#  (უფრო მაღალი/უფრო დაბალი). თამაში აკონტროლებს მცდელობების რაოდენობას და აჩვენებს შედეგს, როდესაც მომხმარებელი გამოიცნობს სწორ რიცხვს.

# თამაში: რიცხვის გამოცნობა
# პროგრამა ირჩევს შემთხვევით რიცხვს და მომხმარებელი ცდილობს მის გამოცნობას
# თამაშს აქვს მინიშნებები რომლებიც აჩვენებენ რამდენად ახლოს ხართ პასუხთან

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
    # თამაშის სტატისტიკა
    games_played = 0
    games_won = 0
    total_attempts = 0
    best_score = float('inf')  # საუკეთესო შედეგი (ყველაზე ცოტა მცდელობა)
    
    print(" კეთილი იყოს თქვენი მობრძანება რიცხვის გამოცნობის თამაშში!")
    
    while True:
        # თამაშის დაწყება
        lower_bound = 1
        upper_bound = 100
        secret_number = random.randint(lower_bound, upper_bound)
        attempts = 0
        games_played += 1

        print("\n" + "=" * 50)
        print(f" თამაში #{games_played} - გამოიცანით რიცხვი {lower_bound} და {upper_bound} შორის.")
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
                    
                    # ვაახლებთ სტატისტიკას
                    games_won += 1
                    total_attempts += attempts
                    
                    # ვამოწმებთ არის თუ არა ახალი რეკორდი
                    if attempts < best_score:
                        best_score = attempts
                        print(f" ახალი რეკორდი!")
                    
                    print("=" * 50)
                    break
            except ValueError:
                print(" გთხოვთ შეიყვანოთ ვალიდური მთელი რიცხვი.")
        
        # ვაჩვენებთ სტატისტიკას თამაშის შემდეგ
        print(f"\n სტატისტიკა:")
        print(f"   ითამაშეთ: {games_played} თამაში")
        print(f"   მოგებული: {games_won} თამაში")
        if games_won > 0:
            average = total_attempts / games_won
            print(f"   საშუალო მცდელობა: {average:.1f}")
            print(f"   საუკეთესო შედეგი: {best_score} მცდელობა")
        
        # ვკითხულობთ გსურთ თუ არა თავიდან თამაში
        play_again = input("\n გსურთ თავიდან თამაში? (დიახ/არა): ").lower()
        if play_again in ['არა', 'ara', 'no', 'n']:
            print("\n" + "=" * 50)
            print("    გმადლობთ თამაშისთვის!")
            print(f"   საბოლოო სტატისტიკა: {games_won}/{games_played} მოგება")
            if best_score != float('inf'):
                print(f"   თქვენი რეკორდი: {best_score} მცდელობა")
            print("=" * 50)
            break


if __name__ == "__main__":
    guess_the_number()