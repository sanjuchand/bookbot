with open("books/frankenstein.txt") as f:
    text = f.read()

wordcount = len(text.split())

print(f"Word count: {wordcount}")


def count_characters(text):
    char_count = {}
    lower = text.lower()

    for char in lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


char_count = count_characters(text)
sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

for char, count in sorted_char_count:
    print(f"'{char}': {count}")
