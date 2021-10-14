#David Bonilla
#CIS2348 Ratner
#PSID:1913106
#imports the files
import csv
#input of the words
input1 = input()

#method adds the words to the lsit to check
with open(input1, 'r') as wordsfile:
    words_reader = csv.reader(wordsfile)
    for row in words_reader:
        list_of_words = row

no_duplicates_in_list = list(dict.fromkeys(list_of_words))
listlength = len(no_duplicates_in_list)

#this prints and counts the amount of duplicated words
for i in range(listlength):
    print(no_duplicates_in_list[i], list_of_words.count(no_duplicates_in_list[i]))
