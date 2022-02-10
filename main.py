file = open("copy-words.txt", "r")

words = set()

for word in file:
    words.add(word)

list_words = list(words)


def not_contains(initial_list, letter):
    li = []
    for w in initial_list:
        if letter not in w:
            li.append(w)
    return li


def contains_different_position(initial_list, letter, position):
    li = []
    for w in initial_list:
        if letter in w and w[position] != letter:
            li.append(w)
    return li


def contains_correct_position(initial_list, letter, position):
    li = []
    for w in initial_list:
        if letter in w and w[position] == letter:
            li.append(w)
    return li


def match_pattern(initial_list, patterns):
    li = initial_list
    for (letter, position, case) in patterns:
        if case == 'b':
            li = not_contains(li, letter)
        elif case == 'y':
            li = contains_different_position(li, letter, position)
        else:
            li = contains_correct_position(li, letter, position)
    return li


list_words = match_pattern(list_words, [('c', 0, 'b'), ('r', 1, 'y'), ('a', 2, 'b'), ('n', 3, 'b'), ('e', 4, 'y')])
print(len(list_words))
print(list_words)
