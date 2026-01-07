from random_word import RandomWords

def play_game():
    r = RandomWords()
    word = r.get_random_word()
    guessed = ["_" for _ in word]
    attempts = 6
    guessed_letters = set()

    while attempts > 0 and "_" in guessed:
        print("\nWord: ", " ".join(guessed))
        print("Missed letters: ", " ".join([g for g in guessed_letters if g not in word]))

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"Incorrect! {attempts} attempts left.")

    if "_" not in guessed:
        print(f"\n🎉 Congrats! You found the word: {word}")
    else:
        print(f"\n💀 Game over! The word was: {word}")

while True:
    play_game()
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing! Goodbye 👋")
        break