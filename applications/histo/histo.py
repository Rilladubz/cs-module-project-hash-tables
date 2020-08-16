# Your code here
with open("robin.txt") as f:
    histo = f.read()

    def histo_func(file):

        words = {}

        remove_white_space = " ".join(file.split())

        bad_chars = ['"', ':', '.', '-', '+', '=', '/', '\\',
                     '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', ',', ';']

        updated_string = ''.join(
            char.lower() for char in remove_white_space if not char in bad_chars)

        word_list = updated_string
        word_list = word_list.split()

        for word in word_list:
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1

        sorted_words = sorted(
            words.items(), key=lambda x: x[-1], reverse=True)
        print(sorted_words)

        for key in words:
            num = words[key]
            hashtag = "#" * num
            words[key] = hashtag


print(histo_func(histo))
