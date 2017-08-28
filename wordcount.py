
def count_words(word_file):
    """Counts words in a file, returns a dict of words and occurances."""

    words = open(word_file)
    word_count = {}

    for line in words.readlines():
        words = line.rstrip()
        words = words.split(" ")

        for w in words:

            if w in word_count:
                word_count[w] += 1
            else:
                word_count[w] = 1

    # for k, v in word_count.items():
    #     print k, v

    for k in word_count:
        value = word_count[k]
        print k, value

    words.close()

count_words('test.txt')