# put your code here.

#Open the  file:

text_file = open("test.txt")

all_words_in_file = []

for line in text_file:

    #Create list of words in line
    line = line.rstrip()
    line = line.split(" ")

    #Add words to master list
    all_words_in_file.extend(line)

word_counts = {}

#Loop over master word list
for word in all_words_in_file:

    #Add new words to dictionary. Otherwise increment count.
    word_counts[word] = word_counts.get(word, 0) + 1

print word_counts



