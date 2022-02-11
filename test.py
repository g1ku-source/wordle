import wordle as wordle

LIST_WORDS = wordle.get_words()


def test():
    number_words = len(LIST_WORDS)
    average = 0

    for word in LIST_WORDS:
        average += 1

        if word == wordle.INITIAL_WORD:
            continue

        pattern = wordle.compute_pattern(word, wordle.INITIAL_WORD)
        li = list(zip(wordle.INITIAL_WORD, wordle.LIST_INDEXES, pattern))

        average += 1

        list_words = wordle.match_pattern(LIST_WORDS, li)
        guessed = wordle.find_word(list_words)
        list_words.remove(guessed)

        while guessed != word:
            pattern = wordle.compute_pattern(word, guessed)
            li = list(zip(guessed, wordle.LIST_INDEXES, pattern))

            list_words = wordle.match_pattern(list_words, li)
            guessed = wordle.find_word(list_words)

            list_words.remove(guessed)
            average += 1

    return average / number_words


print(test())
# 3.615550755939525in average
