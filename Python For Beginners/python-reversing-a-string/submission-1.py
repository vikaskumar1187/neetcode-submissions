def reverse_string(s: str) -> str:
    #return s[::-1]
    start = None
    end = None
    step = -1
    return s[end:start:step]

# do not modify below this line
print(reverse_string("NeetCode"))
print(reverse_string("Hello!"))
print(reverse_string("Bye Bye"))
