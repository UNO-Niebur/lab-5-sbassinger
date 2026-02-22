#Word Game is a knock-off version of a popular online word-guessing game.
#WordGame.py
#Name:Scott Bassinger
#Date:02/22/2026
#Assignment:Lab 5 - WordGame
import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    if (word.find(letter) >= 0):
        return True
    else:
        return False


def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    if (word[spot] == letter):
        return True
    else:
        return False

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    response = ""
    for i in range(len(word)):
        if (inSpot(myGuess[i], word, i)):
            response = response + myGuess[i].upper()
        elif (inWord(myGuess[i], word)):
            response = response + myGuess[i].lower()
        else:
            response = response + "*"
    return response


def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)

    # User should get 6 guesses to guess
    guesses = 6
    attempts = 0
    while attempts < guesses:
        # Ask user for their guess
        myGuess = input("Enter your guess: ")
        # If the guess length is wrong, do not count this as an attempt
        if len(myGuess) != len(todayWord):
            print("Your guess must be", len(todayWord), "letters long.")
            continue
        # If the guess is not a valid word, do not count this as an attempt
        if myGuess not in wordList:
            print("Sorry, that is not a valid word.")
            continue
        # Valid guess counts as an attempt
        attempts += 1
        # Give feedback using on their word:
        feedback = rateGuess(myGuess, todayWord)
        print(feedback)
        if myGuess == todayWord:
            print("Congratulations! You guessed the word.")
            break
    else:
        print("Sorry, you've used all your guesses. The word was:", todayWord)



if __name__ == '__main__':
  main()
