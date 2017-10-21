from PyDictionary import PyDictionary
import string
d=PyDictionary()

sentence = input("Enter your sentence\n>")

list_sentence = sentence.split()
mysyms = []
vowels = ['a','e','i','o','u']
letters_by_score = {}
counter = 0
for i in string.ascii_lowercase: #Creates the map of letters and scores
    counter += 1
    letters_by_score[i] = counter


def get_score(word):
    #Get word's score

    #things that go into finding score:
    #   vowels
    #   length
    #   unique letters in the word
    #   score increase for how late that specific letter appears in the alphabet

    vowels = ['a','e','i','o','u']

    vowelcount = 0
    score = 0

    let_score = 0


    for i in list(word): #gets number of vowels in the word
        if i in vowels:
            vowelcount += 1

        let_score += letters_by_score[i]

    score = let_score + vowelcount + round(len(word) / 2)

    return score






for word in list_sentence: #Go through all words
    syn_list = d.synonym(word)

    if not syn_list == [] or not syn_list == None: #Error catching
        try: #More error catching

            if word.lower() == 'i':

                raise ValueError("We don't want this word to change!")
            largest = syn_list[0]


            for i in syn_list: #Find largest word in synonym list




                if get_score(i) > get_score(largest):
                    largest = i



            mysyms.append(largest)

        except Exception as e:

            mysyms.append(word)

    else:
        mysyms.append(word)

print(mysyms)
