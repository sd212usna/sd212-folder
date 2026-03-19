import re

# Read in words from file into a single list
words = [line.strip() for line in open('10k-words.txt')]
assert len(words) == 10000

def friends(word1, word2):
    """Determines if the two strings are the same except for index 1 and 5.
    For example, 'massive' and 'missile'.
    """
    if len(word1) < 6:
        return False
    pattern = f"^{word1[:1]}[^{word1[1]}]{word1[2:5]}[^{word1[5]}]{word1[6:]}$"
    return re.match(pattern, word2)

def check_words(start_index, end_index):
    """Finds friend words for all words in the given index range."""
    for i in range(start_index, end_index):
        for j in range(i+1, len(words)):
            if friends(words[i], words[j]):
                print(words[i], words[j])

if __name__ == '__main__':
    # There are 10000 words in the list, so this function call gets them all
    check_words(0, 10000)

    print("all friends found")
