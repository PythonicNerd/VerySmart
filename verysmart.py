from PyDictionary import PyDictionary
d=PyDictionary()

sentence = input("Enter your sentence\n>")

list_sentence = sentence.split()
mysyms = []

"""
for word in list_sentence:
    syn_list = d.synonym(word)
    try:
        largest = syn_list[0]
        for i in syn_list:
            if len(i) > len(largest):
                largest = i

            mysyms.append(largest)
    except:
        mysyms.append(word)

"""

for word in list_sentence:
    syn_list = d.synonym(word)

    if not syn_list == [] or not syn_list == None:
        try:
            largest = syn_list[0]


            for i in syn_list:
                if len(i) > len(largest):
                    largest = i

            mysyms.append(largest)`
    else:
        mysyms.append(word)

print(mysyms)
#cycle the words in the sentence
#get the syns of word
#cycle syns to find the biggest word


print(mysyms)
