file = open("words.txt", "r")

words = set()

for word in file:
    if word != "\n":
        words.add(word[0:5])

list_words = list(words)
list_words.sort()
list_words.remove(' \n')


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


# list_words = not_contains(list_words, 'r')
# list_words = not_contains(list_words, 'a')
# list_words = not_contains(list_words, 'n')
# list_words = contains_different_position(list_words, 'c', 0)
# list_words = contains_different_position(list_words, 'e', 4)
# list_words = not_contains(list_words, 'l')
# list_words = not_contains(list_words, 't')
# list_words = not_contains(list_words, 'h')
# list_words = contains_correct_position(list_words, 'd', 0)
# list_words = contains_correct_position(list_words, 'i', 1)
# list_words = contains_correct_position(list_words, 'c', 2)
# list_words = contains_correct_position(list_words, 'e', 3)

list_words = not_contains(list_words, 'c')
list_words = not_contains(list_words, 'n')
list_words = not_contains(list_words, 'b')
list_words = not_contains(list_words, 'l')
list_words = not_contains(list_words, 'i')
list_words = not_contains(list_words, 'm')
list_words = not_contains(list_words, 's')
list_words = not_contains(list_words, 'k')
list_words = contains_different_position(list_words, 'r', 1)
list_words = contains_different_position(list_words, 'a', 2)
list_words = contains_different_position(list_words, 'e', 4)
list_words = contains_correct_position(list_words, 'a', 0)
list_words = contains_correct_position(list_words, 'e', 3)
list_words = contains_correct_position(list_words, 'r', 4)

print(list_words)
