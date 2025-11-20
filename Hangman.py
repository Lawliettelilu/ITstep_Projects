# 2.3 თამაში 2: Hangman
# Hangman არის სიტყვების გამოცნობის თამაში. პროგრამა ირჩევს შემთხვევით სიტყვას წინასწარ განსაზღვრული სიიდან და აჩვენებს მას ქვედა ტირეების გამოყენებით 
# (რამდენი ასოცაა სიტყვაში, იმდენი ქვედა ტირე), რომელიც წარმოადგენს ფარულ ასოებს. 
# მომხმარებლებს სთხოვენ გამოიცნონ ასო და პროგრამა ამოწმებს არის თუ არა ასო სიტყვაში. 
# ვლინდება სწორად გამოცნობილი ასოები და თამაში გრძელდება მანამ, სანამ მომხმარებელი არ გამოიცნობს სიტყვას ან არ ამოიწურება მცდელობები.

import random

# Hangman-ის ვიზუალური სტადიები (6 მცდელობისთვის)
def get_hangman_stage(attempts_left):
    stages = [
        # Stage 0 - Dead (0 attempts left)
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # Stage 1 (1 attempt left)
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # Stage 2 (2 attempts left)
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # Stage 3 (3 attempts left)
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # Stage 4 (4 attempts left)
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # Stage 5 (5 attempts left)
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # Stage 6 (6 attempts left)
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    
    stage_index = 6 - attempts_left
    if stage_index >= len(stages):
        stage_index = len(stages) - 1
    
    return stages[stage_index]

# სიტყვების ლოკალური სია (ვცადეთ API გამოყენება თუმცა დიდი ხნით ფიქრობდა და ამიტომ გადავწყვიტე ლოკალური სიის გამოყენება)
WORD_LIST = [
    "კატა", "ძაღლი", "მზე", "მთვარე", "ვარსკვლავი", "თევზი", "ფრინველი", "ხე",
    "წიგნი", "კალამი", "მანქანა", "ავტობუსი", "სახლი", "სიყვარული", "დრო", "თამაში",
    "პითონი", "კომპიუტერი", "კლავიატურა", "მაუსი", "მონიტორი", "პროგრამა",
    "ინტერნეტი", "ფუნქცია", "ცვლადი", "მთა", "ოკეანე", "ტყე",
    "სპილო", "ვეფხვი", "დელფინი", "პინგვინი", "გიტარა", "პიანინო",
    "შოკოლადი", "პიცა", "ბურგერი", "ყავა", "სენდვიჩი", "ცისარტყელა",
    "ქუხილი", "ბიბლიოთეკა", "ბაღი", "სურათი", "დაბადება", "დღესასწაული",
    "პროგრამირება", "ალგორითმი", "მონაცემთა", "ქსელი",
    "უსაფრთხოება", "პროგრამისტი", "პეპელა", "რევოლუცია", "თავგადასავალი",
    "წარმოსახვა", "არაჩვეულებრივი", "ლამაზი", "დიდებული",
    "საოცარი", "ინტელექტი", "ჩემპიონატი", "იდუმალი",
    "ზეიმი", "მიღწევა", "ტექნოლოგია", "არქიტექტურა",
    "ფოტოგრაფია", "უნივერსიტეტი", "ურთიერთობა", "ენციკლოპედია"
]

# ფუნქცია აბრუნებს შემთხვევით სიტყვას ლოკალური სიიდან
def get_random_word():
    return random.choice(WORD_LIST)

# ფუნქცია მინიშნების მისაღებად
def get_hint(secret_word, displayed_word):
    hidden_indices = [i for i, letter in enumerate(displayed_word) if letter == '_']
    if hidden_indices:
        hint_index = random.choice(hidden_indices)
        return secret_word[hint_index]
    return None

def hangman():
    print("\n" + "=" * 50)
    print("    კეთილი იყოს თქვენი მობრძანება Hangman თამაშში!")
    print("=" * 50)
    
    # თამაშის სტატისტიკა
    games_played = 0
    games_won = 0
    
    while True:
        attempts_left = 6
        secret_word = get_random_word()
        guessed_letters = set()
        displayed_word = ['_' for _ in secret_word]
        hint_used = False

        print("\n" + "=" * 50)
        print(f" თამაში დაიწყო! სიტყვის სიგრძე: {len(secret_word)} ასო")
        print(f" მცდელობები: 6")
        print("=" * 50)

        while attempts_left > 0 and '_' in displayed_word:
            # კაცუნას ჩვენება
            print(get_hangman_stage(attempts_left))
            
            print("\n" + "-" * 50)
            print("სიტყვა:", ' '.join(displayed_word))
            print(f"მცდელობები დარჩენილი: {attempts_left}/6")
            
            if guessed_letters:
                print(f"გამოცნობილი ასოები: {', '.join(sorted(guessed_letters))}")
            
            # ოპციების მენიუ
            print("\n ოპციები:")
            print("  1. ასოს გამოცნობა")
            print("  2. მთელი სიტყვის გამოცნობა")
            if not hint_used and attempts_left > 1:
                print("  3. მინიშნების მიღება (დაგიჯდებათ 1 მცდელობა)")
            
            choice = input("\nაირჩიეთ ოპცია: ")
            
            if choice == '1':
                # ასოს გამოცნობა
                guess = input("გამოიცანით ასო: ")

                if len(guess) != 1 or not guess.isalpha():
                    print(" გთხოვთ შეიყვანოთ ერთი ასო.")
                    continue

                if guess in guessed_letters:
                    print(" თქვენ უკვე გამოიცანით ეს ასო. სცადეთ სხვა.")
                    continue

                guessed_letters.add(guess)

                if guess in secret_word:
                    for idx, letter in enumerate(secret_word):
                        if letter == guess:
                            displayed_word[idx] = guess
                    print(" სწორი ვარაუდი!")
                else:
                    attempts_left -= 1
                    print(" არასწორი ვარაუდი.")
                    
            elif choice == '2':
                # სრული სიტყვის გამოცნობა
                word_guess = input("შეიყვანეთ სიტყვა: ")
                
                if word_guess == secret_word:
                    displayed_word = list(secret_word)
                    print(" ვუუჰუუუ! სწორად გამოიცანით სიტყვა!")
                else:
                    attempts_left -= 1
                    print(" არასწორი სიტყვა!")
                    
            elif choice == '3' and not hint_used and attempts_left > 1:
                # მინიშნის მიღება
                hint_letter = get_hint(secret_word, displayed_word)
                if hint_letter:
                    for idx, letter in enumerate(secret_word):
                        if letter == hint_letter:
                            displayed_word[idx] = hint_letter
                    attempts_left -= 1
                    hint_used = True
                    print(f" მინიშნება: ასო '{hint_letter}' გამოჩნდა!")
            else:
                print(" არასწორი არჩევანი. სცადეთ თავიდან.")

        # თამაშის შედეგი
        print("\n" + "=" * 50)
        games_played += 1
        
        if '_' not in displayed_word:
            print(" გილოცავ! მოიგეთ!")
            print(f" სიტყვა იყო: {secret_word}")
            games_won += 1
        else:
            print(get_hangman_stage(0))
            print(" თქვენ წააგეთ!")
            print(f" სიტყვა იყო: {secret_word}")
        
        # სტატისტიკის ჩვენება
        if games_played > 0:
            win_rate = (games_won / games_played) * 100
            print(f"\n სტატისტიკა: {games_won}/{games_played} მოგება ({win_rate:.1f}%)")
        
        print("=" * 50)
        
        # კიდევ თამაშის კითხვა
        play_again = input("\nგსურთ თავიდან თამაში? (კი/არა): ").lower()
        if play_again not in ['კი', 'k', 'yes', 'y']:
            print("\n" + "=" * 50)
            print("   გმადლობთ თამაშისთვის! ")
            if games_played > 0:
                print(f"   საბოლოო სტატისტიკა: {games_won}/{games_played} მოგება")
            print("=" * 50)
            break

if __name__ == "__main__":
    hangman()