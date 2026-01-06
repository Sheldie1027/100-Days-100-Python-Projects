from random_word import RandomWords
r = RandomWords()

word = r.get_random_word()
guessed = ["_" for _ in word]
attempts = 6

while attempts > 0 and "_" in guessed:
    print("Word: ", " ".join(guessed))
    guess = input("Guess a letter: ")
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"Incorrect! {attempts} attempts left.")

if "_" not in guessed:
    print("Congrats! You found the word:", word)
else:
    print("Game over! The word was:", word)