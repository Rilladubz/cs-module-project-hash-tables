def no_dups(s):
    # Your code here
    word_list = s.split()

    cache = {}

    new_string = ''

    for word in word_list:
        if word not in cache:
            cache[word] = word
            new_string += ''.join(' ' + word)

    split = new_string.split()
    joined = ' '.join(split)

    if len(word_list) < 2:
        return s
    else:
        return joined


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
