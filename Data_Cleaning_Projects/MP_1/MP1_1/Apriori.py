from itertools import permutations
minsup = 771
data = open("categories.txt", "r").readlines()
whole_data = open("categories.txt", "r").read()
patterns = open("patterns.txt", "w")
read_patterns = open("patterns.txt", "r")
category_sets_list_remove_newline = [x.strip('\n') for x in data]
category_set_list_of_lists = [x.split(";") for x in category_sets_list_remove_newline] 

#Get the formatting for the categories into a list of single items
items = []
for i in range(0, len(category_set_list_of_lists)):
    items += (category_set_list_of_lists[i])

#create a set to capture unique length-1 items
unique_items_set = set()
for each_item in items:
    unique_items_set.add(each_item)

#find length-1 frequent items, capture them in a list, write to first patterns file
freq_items = []
for each_unique_item in unique_items_set:
    if items.count(each_unique_item) > minsup:
        freq_items.append(each_unique_item)
        patterns.write(str(items.count(each_unique_item)) + ":" + each_unique_item + '\n')
print(freq_items)
# #----------------------------------------------------------Part 2--------------------------------------------------------------
sorted_freq_items = sorted(freq_items)
frequent_candidates = sorted_freq_items
generated_candidates = set()
frequent_item_sets = 1
no_frequent_items = False
sorted_generated_candidates = set()
k = 2
count = 0
while no_frequent_items == False:
    #Generate k-length Candidates
    for i in range(0, len(frequent_candidates)):
        for j in range(i + 1, len(frequent_candidates)):
            first_candidate = frequent_candidates[i].split(";")
            second_candidate = frequent_candidates[j].split(";")
            candidate = set(first_candidate) | set(second_candidate)
            if ";".join(candidate) not in generated_candidates and len(candidate) == k:
                generated_candidates.add(";".join(candidate))

    frequent_candidates.clear()
    
    #Check Database
    frequent_item_sets = 0
    for cand in generated_candidates:
        if cand not in read_patterns:
            split_candidates = cand.split(';')
            for line in data:
                line_split = line.strip('\n').split(";")
                if all(parts in line_split for parts in split_candidates):
                    count += 1
            if count > minsup:
                frequent_item_sets += 1
                frequent_candidates.append(cand)
                #combs = list(map(list, permutations(split_candidates, 3)))
                print(cand)
                if (cand not in read_patterns):
                    patterns.write(str(count) + ":" + cand + '\n')
                count = 0
            else:
                count = 0
                pass
    
    generated_candidates.clear()

    # #Check to terminate loop and update k
    if frequent_item_sets == 0:
        no_frequent_items = True

    k += 1
