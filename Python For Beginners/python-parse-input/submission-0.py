from typing import List

def read_integers() -> List[int]:
    n = []
    str_nums = input().split(",")

    for num in str_nums:
        n.append(int(num))
    return n

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
