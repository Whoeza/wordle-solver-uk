# UK dictionary from: https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt

# Step 0.
# Initialize some variables

# Counters for each letter that will track how many times this letter is seen in the input dictionary
# letters_stats = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#                  'u', 'v', 'w', 'x', 'y', 'z']
letters_stats = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
                 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
for letter in letters_stats:
    letters_stats[letter] = 0

# Step 1.
# Calculate statistics for each letter of the alphabet A-Z

# Adding +1 to each letters counter when that letter is found in the input dictionary
file_name = 'uk-dict.txt'
wordle_dict = []
with open(file_name, "r") as dict_file:
    for line in dict_file:
        wordle_dict.insert(len(wordle_dict), line)
for word in wordle_dict:
    for letter in word:
        if '\n' != letter:
            letters_stats[letter] = letters_stats[letter] + 1

# Step 2.
# Assign a score to each word based on how many different letters they have from the subset of most common ones
# (for future reference: is there a better strategy when taking into account all the rules and constraints of the game?)

# Words will be sorted by this score to determine the best starting word from the input dictionary
# The sum of the # of appearances in the whole dictionary for each letter is the score of the word
word_scores = []
for word in wordle_dict:
    word_scores.insert(len(word_scores), word)
    index_of_this_word = word_scores.index(word)
    word_scores[index_of_this_word] = 0
    different_letters = []
    # No further score is added if a letter is seen more than once in the word
    for letter in word:
        if '\n' != letter:
            if letter not in different_letters:
                different_letters.insert(len(different_letters), letter)
                letter_score_increment = letters_stats[letter]
            else:
                letter_score_increment = 0
            word_scores[index_of_this_word] = word_scores[index_of_this_word] + letter_score_increment
# Step 3.
# Print the best starting word for the input dictionary

max_score = 0
for score in word_scores:
    if max_score < score:
        max_score = score

best_word = wordle_dict[word_scores.index(max_score)]
print("The best word is %s with a score of %d" % (best_word, max_score))
# instead of finding ONE best word, let's find ALL best words with the same high-score
# best_words = []
# best_words = [word for word in wordle_dict if max_score == word_scores[wordle_dict.index(word)]]
# print("But the best words are")
# for word in best_words:
#     print(word)
print("Top scores in the input dictionary:")
word_scores.sort()
word_scores.reverse()
print(word_scores[0], word_scores[1], word_scores[2])

if input("Do you want to print the 10 top words? Type y or Y\n") in ['y', 'Y']:
    print("word    score")
    # print first 10 words and scores
    for index in range(10):
        curr_score = word_scores[index]
        curr_word = wordle_dict[word_scores.index(curr_score)]
        print("%s    %d" % (curr_word, curr_score))

#  For the future: make an interactive solver, that provides an answer based on which letters have been already used
