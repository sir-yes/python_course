import random
import words
#word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(words.word_list)
print("Solution is: ",chosen_word)

word_length = len(chosen_word)
display = list("_" * word_length)
guess_history = []
lives = 6
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter:\n").lower()

    while guess in guess_history:
        print("You have already guessed this letter! Please choose a different letter")
        guess = input("Guess a letter:\n").lower()
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word.")
        if lives == 0:
            end_of_game = True
            print("You Lose")
            
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
    print(f"{' '.join(display)}")
    print("Lives left",lives)
    
    if "_" not in display:
        end_of_game = True
        print("You win")
    guess_history.append(guess)
        
# Alternative Checker I made that is a little more concise
'''
while "_" in display:
    guess = input("Guess a letter:\n").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        print("You win")
'''
# Alternative to above using a counter
'''
display1 = list("_" * len(chosen_word))
count = 0
for i in chosen_word:
    if i == guess:
        display1[count] = i
        count += 1
    else:
        count += 1
        
print(display1)
'''