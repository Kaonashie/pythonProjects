words = "Welcome to the secret shop"


def spin_words(sentence):
    words_after = []
    word_count = 0
    e = sentence.split()
    for i in e:
        word_count += 1
    for i in e:
        char_count = 0
        b = i
        for z in b:
            char_count += 1
        if word_count >= 1 and char_count >= 5:
            b = i[::-1]
            s = str(b) + " " + str(char_count)
            # print(s)
            words_after.append(b)
            continue
        else:
            s = str(b) + " " + str(char_count)
            # print(s)
            words_after.append(b)
    concat = ' '.join(str(i) for i in words_after)
    print(concat)


spin_words(words)
