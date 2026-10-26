from typing import List

def contains_duplicate(words: List[str]) -> bool:
    lw = len(words)
    s = set()
    for i in range(lw) :
        s.add(words[i])

    ls = len(s)

    return lw != ls

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
