# UK dictionary from: https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt

# Step 0.
# Initialize some variables

# Counters for each letter that will track how many times this letter is seen in the input dictionary
letters_stats = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
for letter in letters_stats:
    letters_stats[letter] = 0

# Step 1.
# Calculate statistics for each letter of the alphabet A-Z

# Adding +1 to each letters counter when that letter is found in the input dictionary
file_name = 'uk-dict.txt'
wordle_dict = []
with open(file_name, "r") as dict_file:
    for line in dict_file:
        wordle_dict.insert(line)
for word in wordle_dict:
    for letter in word:
        letters_stats[letter] = letters_stats[letter] + 1

# Step 2.
# Assign a score to each word based on how many different letters they have from the subset of most common ones
# (for future reference: is there a better strategy when taking into account all the rules and constraints of the game?)

# Words will be sorted by this score to determine the best starting word from the input dictionary
# The sum of the # of appearances in the whole dictionary for each letter is the score of the word
word_scores = []
for word in wordle_dict:
    word_scores.insert(word)
    word_scores[word] = 0
    for letter in word:
        word_scores[word] = word_scores[word] + letters_stats[letter]
word_scores.sort()

# Step 3.
# Print the best starting word for the input dictionary
print(word_scores[1], word_scores[2], word_scores[3])
