import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):": "make a class named %%% that is-a %%%",
    "class %%%(object):\ndef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\ndef ***(self, @@@)":
        "class %%% has-a *** that takes self and @@@ parameters.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function,and call it with parameters self, @@@.",
    "***.*** = '***'":
        "From *** get the attribute and set it to '***'."
}

PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv == "english":
    PHRASE_FIRST = True

for word in urlopen(WORD_URL).readlines():
    # 函数strip()作用为去除字符串首尾空格（没有参数的时候）
    WORDS.append(word.strip().decode('utf-8'))

def convert(snippet, phrase):
    # sample(list，k)函数表示从列表中随机获取k个元素
    # capitalize()实现字符串首字母大写，其余小写
    # count()，统计某个元素在列表中出现的次数
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]  # 列表生成式
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        # random.randint(1, 3)指随机生成1-3范围内的数（1<=x<=3）
        param_count = random.randint(1, 3)
        param_names.append(','.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        # sentence[:]复制列表
        result = sentence[:]

    for word in class_names:
        # repalce()，字符串替换，1指替换次数最多不超过1次
        result = result.replace("%%%", word, 1)

    for word in other_names:
        result = result.replace("***", word, 1)

    for word in param_names:
        result = result.replace("@@@", word, 1)

    results.append(result)
    return results


try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print("answer:{}\n\n".format(answer))
except EOFError:
    print("\nBye")
