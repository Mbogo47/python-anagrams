def find_anagrams(word_1, word_2):
    return sorted(word_1)==sorted(word_2)

print(find_anagrams("racecar","hello" ))