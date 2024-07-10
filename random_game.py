import random
def shuffle_word(word):
    """Shuffle the letters of a word to create an anagram."""
    word = list(word)
    random.shuffle(word)

    return ''.join(word)

def play_anagram_game(words):
    """play anagram game with the given list of words."""
    word = random.choice(words)
    anagram = shuffle_word(word)
    print("welcome to the anagram game!")
    print(f"here is your anagram: {anagram}")

    guess = input("What is the original word? ")

    if guess.lower() == word.lower():
        print("Correct!")
        #ask if the player wants to play again
        print("want to play again? y/n")
        if input().lower() == "y":
            play_anagram_game(words)
        else:
            print("Thanks for playing!")

    else:
        print(f"Sorry, the word was {word}")
        print("want to play again? y/n")
        if input().lower() == "y":
            play_anagram_game(words)
        else:
            print("Thanks for playing!")

#main function
if __name__ == "__main__":
    #add words to the list
    word_list = ["python", "jumble", 
                 "easy", "difficult", 
                 "answer", "xylophone",
                 "apple", "orange",
                 "elephant", "tiger",
                 "xeon","carbon","hydrogen",
                 "oxygen","nitrogen","helium",
                 "lithium","beryllium","boron",
                 "carbon","nitrogen","oxygen",
                 "fluorine","neon","sodium",]
    play_anagram_game(word_list)