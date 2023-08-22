import random
from hangman_art import logo, stages
from hangman_words import word_list

# word_list = ["aardvark", "baboon", "camel"]
print(logo)

chosen_word = random.choice(word_list)
lives = 6
print(f"You start with {lives} lives")

display = list()
for _ in chosen_word:
    display.append("_")

continue_game = True

while continue_game:
    guess = input("Guess a letter in the chosen word: ").lower()
    ind = 0
    found_letter = False
    for letter in chosen_word:

        if letter == guess:
            found_letter = True
            if guess in display:
                print(display)
                print(f"You already proposed letter '{letter}'!")
            else:
                display[ind] = letter
        

        ind += 1

    if not found_letter:
        print(stages[lives])
        lives-=1
        print(f"You typed '{guess}', that is not in the chosen word, you lose a life. You have {lives} lives/life left.")

    print(display)

    if lives == 0 or "_" not in display:
        continue_game = False

if lives != 0 :
    print("You win!")
else:
    print(stages[lives])
    print(f"You lose! the chosen word was {chosen_word}")
        