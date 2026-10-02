def remove_fourth_character(s: str) -> str:
    first = s[:3]
    second = s[4:]

    return first + second

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
