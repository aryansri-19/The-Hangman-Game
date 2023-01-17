#Hangman Game
import random
#Printing Hangman
def hangman(counter):
    if counter == 1:
        print(" ( )  \n /|\ \n / \\")
    elif counter == 2:
        print("\n |\n |\n | ( )\n | /|\ \n | / \\ ")
    elif counter == 3:
        print(" _____\n |\n |\n | ( )\n | /|\ \n | / \\ ")
    elif counter == 4:
        print(" _____\n |  |\n |\n | ( )\n | /|\ \n | / \\ ")
    elif counter == 5:
        print(" _____\n |  |\n |  |\n | ( )\n | /|\ \n | / \\ ")
    else:
        print(" _____\n |  |\n | ( )\n | /|\ \n | / \\\n | ")

#The actual game function
def game():
    print("Starting the game......\n\nThe word is - ", end="")
    words = []
    with open('Python\wordList.txt', 'r') as file:
        for line in file:
            for word in line.split():
                words.append(word)
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    used_letters = set()
    word = random.choice(words)
    original_letters = set(word)
    correct_letters = set()
    counter = 0
    for _ in word:
        print("_ ", end="")
    while original_letters != correct_letters:
        letter = input("\n\nGuess the letters of the word: ").lower()
        if letter not in alphabets:
            print("Invalid character. Try Again")
        if letter in used_letters:
            print("Already guessed this letter. Try a differenet one...")
        elif letter not in original_letters:
            counter += 1
            print("Incorrect guess...")
            used_letters.add(letter)
            hangman(counter)
            if counter == 6:
                print("And you killed him. Thanks for that, dumbass...\nThe word was "+word)
                return
        else:
            print("Correct guess. The word is: ", end="")
            used_letters.add(letter)
            correct_letters.add(letter)
            for i in word:
                if i in used_letters:
                    print(f"{i} ", end="")
                else:
                    print("_ ", end="")
    
    print("\n\nWhoosh, you saved him from dying. Thanks for playing.")

#The main function
def main():
    print("-------HANGMAN GAME-------\n\nWould you like to play? ")
    choice = input("Enter (Y) for Yes and (N) for No: ").lower()
    if choice == 'y':
        game()
    else:
        exit

if __name__ == '__main__':
    main()
