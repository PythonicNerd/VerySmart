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


print(mysyms)
