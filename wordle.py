import math

file = open("words.txt", "r")
NUMBER_PATTERNS = 242
INITIAL_WORD = "raise"
LIST_INDEXES = [0, 1, 2, 3, 4]


def get_words():
    words = set()
    for word in file:
        words.add(word[0:5])
    return list(words)


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


def ternary(n):
    if n == 0 or n > NUMBER_PATTERNS:
        return '00000'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    while len(nums) < 5:
        nums.append('0')
    return ''.join(reversed(nums))


def ternary_to_pattern(list_characters):
    li = []
    for i in range(0, 5):
        if list_characters[i] == '0':
            li.append('b')
        elif list_characters[i] == '1':
            li.append('y')
        else:
            li.append('g')
    return li


def compute_probability(initial_list, guess):
    list_probability = []
    length = len(initial_list)
    list_index = [0, 1, 2, 3, 4]
    for i in range(0, NUMBER_PATTERNS + 1):
        pattern = zip(guess, LIST_INDEXES, ternary_to_pattern(ternary(i)))
        pattern = list(pattern)
        li = match_pattern(initial_list, pattern)
        list_probability.append((len(li) / length, pattern))

    return list_probability


def calculate_logarithm(probability):
    if probability == 0:
        return 0
    return math.log2((1 / probability))


def compute_expected_value(initial_list, guess):
    list_probability = compute_probability(initial_list, guess)
    expected_value = 0
    for (probability, pattern) in list_probability:
        expected_value += probability * calculate_logarithm(probability)
    return expected_value


def find_word(initial_list):
    expected_value_max = -1
    actual_word = ''
    for wo in initial_list:
        exp = compute_expected_value(initial_list, wo)
        if exp > expected_value_max:
            expected_value_max = exp
            actual_word = wo
    return actual_word


def compute_pattern(word, guess):
    pattern = []
    for i in range(0, 5):
        if guess[i] in word:
            if guess[i] == word[i]:
                pattern.append('g')
            else:
                pattern.append('y')
        else:
            pattern.append('b')
    return pattern
