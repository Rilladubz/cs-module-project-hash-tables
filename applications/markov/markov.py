import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

    words_removed_white_spaces = ' '.join(words.split())

    parsed_words = words_removed_white_spaces.split()

    bad_chars = ['"', ':', '.', '-', '+', '=', '/', '\\',
                 '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', ',', ';']

    start_words = ''

    for first_let in parsed_words:
        if first_let[0] == first_let[0].upper() and first_let[0] not in bad_chars and first_let not in start_words:
            start_words += ''.join(' ' + first_let)

    altered_cap = start_words.split()
    start_words = tuple(altered_cap)

    stop_chars = ['.', '!', '?', ]

    stop_words = ''

    for last_char in parsed_words:
        if last_char[len(last_char) - 1] in stop_chars and last_char not in stop_words:
            stop_words += ''.join(' ' + last_char)

    altered_stop = stop_words.split()
    stop_words = tuple(altered_stop)

    # TODO: analyze which words can follow other words
    # Your code here

    word_model = {}

    for word in parsed_words:
        if word not in word_model:
            word_model[word] = None

    for i in range(len(parsed_words) - 1):
        if parsed_words[i] in word_model and word_model[parsed_words[i]] == None:
            word_model[parsed_words[i]] = parsed_words[i + 1]
        else:
            word_model[parsed_words[i]] += ''.join(' ' + parsed_words[i + 1])

    for word in word_model:
        if word_model[word] is not None:
            update = word_model[word].split()
            altered = tuple(update)
            word_model[word] = altered

    # TODO: construct 5 random sentences

    def generate_Random():
        global start_words
        global stop_words
        global word_model

        starting_word = random.choice(start_words)

        random_sentence = ''

        key = random.choice(list(word_model))
        tuple_list = word_model[key]
        current_word = random.choice(tuple_list)

        random_sentence += ''.join(starting_word)

        while current_word in word_model:
            key = random.choice(list(word_model))
            tuple_list = word_model[key]
            current_word = random.choice(tuple_list)
            random_sentence += ''.join(' ' + current_word)
            if current_word in stop_words:
                return random_sentence

        return random_sentence

    # Your code here
    print(generate_Random())
    # print(generate_Random())
    # print(generate_Random())
    # print(generate_Random())
    # print(generate_Random())
