def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)
        display = ""
        for char in secret_word:
            if char in guesses:
                display += char
            else:
                display += "_"
        print(display)
        return "_" not in display
    return hangman_closure

secret_word = input("Enter a secret word: ")
guess = make_hangman(secret_word)

done = False
while not done:
    letter = input("Guess a letter: ")
    done = guess(letter)

print("You guessed the secret word")