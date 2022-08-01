import random
import art
import words

print(art.logo)

chosen_word = random.choice(words.word_list)
print(chosen_word)

letter_length = len(chosen_word)
display = list("_" * letter_length)
print(display)

lives = 6

end_game = False

while not end_game:

    guess = input("Guess a letter:\n").lower()

    if guess in display:
        print("Silly sausage, you've already guessed that one!")

    for position in range(letter_length):
        if chosen_word[position] == guess:
            display[position] = guess

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the word. You lost a life.")
        print(art.stages[lives])
        if lives == 0:
            end_game = True
            print("Sorry pal, you lose.")

    if "_" not in display:
        end_game = True
        print("Aye, you win!")
