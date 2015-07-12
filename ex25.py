def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words  # 返回一个列表


def sort_words(words):
    """Sorts the words"""
    return sorted(words)  # 返回经过排序的句子


def print_first_word(words):
    """Prints the first word after popping it off"""
    word = words.pop(0)  # 这里words是一个列表，pop函数用来弹出指定位置的元素
    print(word)


def print_last_word(words):
    """Prints the last word after popping it off"""
    word = words.pop(-1)  # 负索引，pop(-1)表示弹出倒数第一个元素
    print(word)


def sort_sentence(sentence):
    """Take in a full sentence and return the sorted words"""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
