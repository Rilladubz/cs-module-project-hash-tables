def word_count(s):
    # Your code here

    # If there are any white space this will remove them
    remove_white_space = " ".join(s.split())
    # List of bad characters to ignore
    bad_chars = ['"', ':', '.', '-', '+', '=', '/', '\\',
                 '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', ',', ';']
    # removes bad characters from string.
    updated_strings = ''.join(
        char for char in remove_white_space if not char in bad_chars)
    # creates a list of the updated strings
    words_list = updated_strings.split()
    words = {}

    for word in words_list:
        lower_word = word.lower()
        if lower_word not in words:
            words[lower_word] = 1
        else:
            words[lower_word] += 1

    if len(words) == 0:
        return {}
    else:
        return words


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
