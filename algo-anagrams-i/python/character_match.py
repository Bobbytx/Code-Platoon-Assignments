# Don't forget to run the tests (and create some of your own)

# Part 1
def is_character_match(string1, string2):
	word1 = string1.lower()
	word2 = string2.lower()

	return sorted(word1) == sorted(word2)

#print(is_character_match('cha4rm', 'm4arch'))

# Part 2
def anagrams_for(word, list_of_words):
	anagrams = []
	for w in list_of_words:
		if is_character_match(word, w):
			anagrams.append(w)
	return anagrams

#print(anagrams_for("saltier", ["cognac", "saltier", "realist", "retails"]))
