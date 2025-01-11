#!/usr/bin/python3

import argparse


def generate_root_list_lowercase(wordlist):
    """
    Reads a file and returns a list of lowercase names.
    Skips empty lines.
    """
    names = []
    try:
        with open(wordlist, 'r') as f:
            for line in f:
                stripped_line = line.strip().lower()
                if stripped_line:  # Skip empty lines
                    names.append(stripped_line)
    except FileNotFoundError:
        print(f"Error: File '{wordlist}' not found.")
        exit(1)
    return names


def lowercase_transformations(names):
    """
    Prints lowercase username transformations.
    Skips lines with less than two words.
    """
    for line in names:
        words = line.split()
        if len(words) < 2:
            print(f"Skipping line: '{line}' (not enough words)")
            continue
        print(words[0])                             # john lennon -> john
        print(words[1])                             # john lennon -> lennon
        print(words[0][0] + '.' + words[1])         # john lennon -> j.lennon
        print(words[0][0] + '-' + words[1])         # john lennon -> j-lennon
        print(words[0][0] + '_' + words[1])         # john lennon -> j_lennon
        print(words[0][0] + '+' + words[1])         # john lennon -> j+lennon
        print(words[0][0] + words[1])               # john lennon -> jlennon
        print(words[0] + words[1])                  # john lennon -> johnlennon
        print(words[1] + words[0])                  # john lennon -> lennonjohn
        print(words[0] + '.' + words[1])            # john lennon -> john.lennon
        print(words[1] + '.' + words[0])            # john lennon -> lennon.john


def uppercase_transformations(names):
    """
    Prints uppercase username transformations.
    Skips lines with less than two words.
    """
    for line in names:
        words = line.split()
        if len(words) < 2:
            print(f"Skipping line: '{line}' (not enough words)")
            continue
        first_word = words[0]
        second_word = words[1]
        print(first_word.capitalize())                                  # john lennon -> John
        print(second_word.capitalize())                                 # john lennon -> Lennon
        print(first_word[0].upper() + '.' + second_word.capitalize())   # john lennon -> J.Lennon
        print(first_word[0].upper() + '_' + second_word.capitalize())   # john lennon -> J_Lennon
        print(first_word[0].upper() + '-' + second_word.capitalize())   # john lennon -> J-Lennon
        print(first_word[0].upper() + second_word.capitalize())         # john lennon -> JLennon
        print(first_word.capitalize() + second_word.capitalize())       # john lennon -> JohnLennon
        print(second_word.capitalize() + first_word.capitalize())       # john lennon -> LennonJohn
        print(first_word.upper())                                       # john lennon -> JOHN
        print(second_word.upper())                                      # john lennon -> LENNON
        print(first_word.upper() + second_word.upper())                 # john lennon -> JOHNLENNON


if __name__ == "__main__":
    # Argument parser setup
    parser = argparse.ArgumentParser(
        description='Python script to generate user lists for bruteforcing!'
    )
    parser.add_argument('-w', '--wordlist', type=str, required=True,
                        help="Specify path to the wordlist")
    parser.add_argument('-u', '--uppercase', action='store_true',
                        help='Also produce uppercase permutations. Disabled by default')

    args = parser.parse_args()

    # Generate lowercase names list
    names = generate_root_list_lowercase(args.wordlist)

    # Perform transformations
    lowercase_transformations(names)

    if args.uppercase:
        uppercase_transformations(names)
