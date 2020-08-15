import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

    # remove white spaces
    words_removed_white_spaces = ' '.join(words.split())
    # print(words_removed_white_spaces)

    parsed_words = words_removed_white_spaces.split()
    # print(parsed_words)

    # Capped_words = {}

    # for first_let in parsed_words:
    #     if first_let[0] == first_let[0].upper() and first_let not in Capped_words:
    #         Capped_words[first_let] = first_let

    # print(Capped_words)

    # TODO: analyze which words can follow other words
    # Your code here

    word_model = {}

    for word in parsed_words:
        if word not in word_model:
            word_model[word] = []

    print(word_model)

    # for i in range(len(parsed_words) - 1):
    # if parsed_words[i] not in word_model:
    # word_model[parsed_words[i]] = parsed_words[i + 1]

    for i in range(word_model - 1)

    # TODO: construct 5 random sentences
    # Your code here
