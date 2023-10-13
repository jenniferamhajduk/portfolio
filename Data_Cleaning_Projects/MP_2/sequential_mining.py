minsup = 100
patterns = open("patterns.txt", "w")
data = open("reviews.txt", "r").read()
data_lines = open("reviews.txt", "r").readlines()
lines_of_word_strings = [line.strip('\n').split(' ') for line in data_lines]
database_prefixes = set()
database_suffices = []

for line in lines_of_word_strings:
    for word in line:
        database_prefixes.add(word)

for prefix in database_prefixes:
    if data.count(prefix) >= minsup:
        patterns.write(str(data.count(prefix)) + ":" + prefix + '\n')