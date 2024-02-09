# task2 : Breaking Real Hashes.
# Ethan Swenke and HanYu Wu
# CSC-321-03

# STEPS:
    # take the bcrypt file and collect each users salt and hash
    # recommended to split hashses up in groups based on workfactor
    # for all 6 to 10 letter words in the words.words() list:
        # checkpw() args are IN BYTES i.e. b"<insert arg here>" 
        # checkpw() takes in the word as the first param, then the entire hash as the second param
        # if checkpw() returns true, the password has been cracked

from bcrypt import *
from nltk.corpus import words


def read_shadow():
    try:
        with open("shadow.txt", 'r') as file:
            for line in file:
                # Process each line as needed
                process_line_data(line)
    except FileNotFoundError:
        print(f"File 'shadow.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def brute_force(line):
    # for each word in the words list
        # run checkpq(b"word", b"hash") for the given user past the colon
    
    words = get_words()
    user_hash = bytes(line[(line.find(':')+1):])
    for word in words:
        if checkpw(bytes(word), user_hash):
            return True


def get_words():
    # filter words list down to words of only 6 to 10 letters

    words = words.words()
    filtered_words = list(filter(lambda x: 6 <= len(x) <= 10, words))
    return filtered_words

