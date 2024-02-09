# task2 : Breaking Real Hashes.
# Ethan Swenke and HanYu Wu
# CSC-321-03

from bcrypt import *
from nltk.corpus import words
import time


def read_shadow():
    try:
        with open("shadow.txt", 'r') as file:
            lines = file.read().splitlines()
            for line in lines:
                print(brute_force(line))
    except FileNotFoundError:
        print(f"File 'shadow.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def brute_force(line):
    # for each word in the words list
        # run checkpq(b"word", b"hash") for the given user past the colon

    start_time = time.time() 
    words = get_words()
    user = line[:line.find(':')]
    user_hash = line[(line.find(':')+1):].encode('utf-8')

    for word in words:
        if checkpw(word.encode('utf-8'), user_hash):
            end_time = time.time()  # Record the end time
            elapsed_time = end_time - start_time
            print(user + "'s password: " + word)
            print("crack time: " + str(elapsed_time))
            return True
    return False


def get_words():
    # filter words list down to words of only 6 to 10 letters

    valid_words = words.words()
    filtered_words = list(filter(lambda x: 6 <= len(x) <= 10, valid_words))
    return filtered_words

if __name__ == "__main__":
    print(read_shadow())