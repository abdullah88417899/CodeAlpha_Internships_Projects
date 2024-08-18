import random
from colorama import Fore, Style, init

init()

words = ["play", "game", "globe", "jave", "pakistan", "cricket", "basketball"]
guessed_letters = []



def get_guesses(user_guess, chosen_word, secret_word, attempts):
    if user_guess == "exit":
        print("\n🚪 Thanks for playing! Goodbye. 👋")
        exit()

    if user_guess.isdigit():
        print(Fore.RED + "\n🚫 Sorry, you can't enter a digit. ❌" + Style.RESET_ALL)
        return False, attempts

    if not user_guess:
        print(Fore.YELLOW + "\n📝 You must enter at least one letter." + Style.RESET_ALL)
        return False, attempts

    if len(user_guess) != 1:
        print(Fore.BLUE + "\n⚠️ Sorry, you have to enter one letter at a time." + Style.RESET_ALL)
        return False, attempts

    if user_guess in guessed_letters:
        print(Fore.YELLOW + f"\n🔄 You have already guessed '{user_guess}'. Try a different one." + Style.RESET_ALL)
        return False, attempts

    guessed_letters.append(user_guess)

    if user_guess in chosen_word:
        print(Fore.GREEN + "\n🎉 Wow! You guessed a letter correctly. Keep it up! 💪" + Style.RESET_ALL)
        for idx, letter in enumerate(chosen_word):
            if letter == user_guess:
                secret_word[idx] = user_guess
        return True, attempts
    else:
        print(Fore.RED + f"\n❌ Sorry, '{user_guess}' is not in the word. Try again." + Style.RESET_ALL)
        attempts -= 1
        print(Style.BRIGHT + f"\n🔢 Remaining attempts: {attempts}" + Style.RESET_ALL)
        return False, attempts
        

def play_game():
    chosen_word = random.choice(words)
    secret_word = ['_' for _ in chosen_word]
    attempts = 10
    guessed_letters.clear()

    user_name = input("\n👤 Please enter your name: ")
    print(f"\nHi {user_name}, let's start the game! 🎉")

    while True:
        print(f"\n🕵️‍♂️ The Secret Word is: {' '.join(secret_word)}")
        user_guess = input("\nEnter your guess: ").lower()

        correct_guess, attempts = get_guesses(user_guess, chosen_word, secret_word, attempts)

        if correct_guess:
            if '_' not in secret_word:
                print(Fore.GREEN + f"\n🎊 Congratulations {user_name}! You guessed the word: {''.join(secret_word)} 🎉 " + Style.RESET_ALL)
                break
        else:
            if attempts <= 0:
                print(Fore.RED + f"\n😢 Sorry {user_name}, you've run out of attempts. The word was '{chosen_word}'. Better luck next time! 🍀" + Style.RESET_ALL)
                break




def replay():
    
    while True:
        
        replay_request = input("\nWanna play again? (y/n): ").lower()

        if replay_request == "n":
            print(Fore.GREEN + "\nSure, see you next time! 👋" + Style.RESET_ALL)
            break
        if replay_request == "y":
            play_game()

        else:
            print("Invalid input. Please enter 'y' or 'n'.")



if __name__ == "__main__":

    print("🎮 Welcome to the Hangman Game! 🎮")
    print("+_________________________________+")
    print("\nGuidlines:\n")
    print("1️⃣ You've to guess the letter of a secret word.")
    print("2️⃣ You've 10 attempts to guess the right word.")
    print("3️⃣ You can enter only one letter at a time.")
    print("4️⃣ You can type 'exit' to exit the game.")

    play_game()
    replay()
