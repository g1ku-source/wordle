import wordle

list_words = wordle.get_words()
list_words = wordle.match_pattern(list_words, [('r', 0, 'b'), ('a', 1, 'y'), ('i', 2, 'b'), ('s', 3, 'y'), ('e', 4, 'e')])
list_words = wordle.match_pattern(list_words, [('s', 0, 'g'), ('l', 1, 'b'), ('a', 2, 'g'), ('t', 3, 'b'), ('e', 4, 'g')])
list_words = wordle.match_pattern(list_words, [('s', 0, 'g'), ('p', 1, 'b'), ('a', 2, 'g'), ('d', 3, 'b'), ('e', 4, 'g')])
# list_words = wordle.match_pattern(list_words, [('c', 0, 'b'), ('h', 1, 'b'), ('a', 2, 'y'), ('r', 3, 'g'), ('t', 4, 'y')])
#list_words = wordle.match_pattern(list_words, [('a', 0, 'y'), ('l', 1, 'b'), ('e', 2, 'g'), ('r', 3, 'y'), ('t', 4, 'g')])
print(wordle.find_word(list_words))
