import nltk
from nltk.corpus import wordnet
import os

# Download the WordNet data
##nltk.download('wordnet')


def get_word_info():
    word = input("\nEnter a word to search (e.g., 'happy', 'fast', 'big'): ")
    synsets = wordnet.synsets(word)

    if synsets:
        # Print Definitions
        definitions = [synset.definition() for synset in synsets]

        # Print Synonyms
        synonyms = set()
        for synset in synsets:
            synonyms.update([lemma.name() for lemma in synset.lemmas()])

        # Print Antonyms
        antonyms = set()
        for synset in synsets:
            antonyms.update([
                antonym.name() for lemma in synset.lemmas()
                for antonym in lemma.antonyms()
            ])

        # Print Examples
        examples = set()
        for synset in synsets:
            examples.update([example.replace('_', ' ') for example in synset.examples()])

        # Save to history.txt
        with open('history.txt', 'a') as file:
            file.write(f"\nWord: {word}\n")
            file.write(f"Definitions: {', '.join(definitions)}\n")

            if synonyms:
                file.write(f"Synonyms: {', '.join(synonyms)}\n")
            else:
                file.write("No Synonyms available\n")

            if antonyms:
                file.write(f"Antonyms: {', '.join(antonyms)}\n")
            else:
                file.write("No Antonyms available\n")

            if examples:
                file.write(f"Examples: {', '.join(examples)}\n")
            else:
                file.write("No Examples available\n")

            file.write("-" * 50)

        print(f"\nDefinitions for '{word}': {', '.join(definitions)}\n")

        if synonyms:
            print(f"Synonyms for '{word}': {', '.join(synonyms)}\n")
        else:
            print(f"No Synonyms available for '{word}'.\n")

        if antonyms:
            print(f"Antonyms for '{word}': {', '.join(antonyms)}\n")
        else:
            print(f"No Antonyms available for '{word}'.\n")

        if examples:
            print(f"Examples for '{word}': {', '.join(examples)}\n")
        else:
            print(f"No Examples available for '{word}'.\n")
    else:
        print(f"Sorry, couldn't find information for '{word}'.\n")
    choice = input("Press'Enter' to continue or break press any key")
    if choice == '':
        get_word_info()


def view_history():
    if os.path.exists('history.txt'):
        with open('history.txt', 'r') as file:
            history_data = file.read()
            if history_data:
                print("\nSearch History:")
                print(history_data)
            else:
                print("\nSearch history is empty.")
    else:
        print("\nSearch history file not found.\nPlease create some history.")


def clear_history():
    if os.path.exists('history.txt'):
        with open('history.txt', 'r') as file:
            history_data = file.read()
            if history_data:
                # Backup existing history to backup.txt
                with open('backup.txt', 'a') as backup_file:
                    backup_file.write(history_data)

                # Clear history.txt
                with open('history.txt', 'w') as clear_file:
                    clear_file.write("")

                print("\nSearch history cleared. Backup saved in backup.txt.")
            else:
                print("\nSearch history is already empty.")
    else:
        print("\nSearch history file not found.")


if __name__ == "__main__":
    name = input('Enter your name: ')
    print(f"Welcome {name} to Apna Dictionary!")

    while True:
        print("\nOptions:")
        print("1. Search")
        print("2. View History")
        print("3. Clear History")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            get_word_info()
        elif choice == '2':
            view_history()
        elif choice == '3':
            clear_history()
        elif choice == '4':
            print(f"See you next time, {name}!")
            break
        else:
            print(f"Invalid choice {name}. Try again.")
