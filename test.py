text=''
with open('file_example_CSV_5000.csv', 'r') as f:
    for line in f:
        text+=line

def letter_occurence(word):
    letter_dict={}
    for letter in word:
        if letter in letter_dict:
            letter_dict[letter]+=1
        else:
            letter_dict[letter]=1
    #print(letter_dict)
    sort_dict = sorted(letter_dict.items(), key=lambda x: x[1], reverse=True)
    output=''
    for key, value in sort_dict:
        if key == ',' or key == '\n':
            continue
        elif key != ' ':
            output+= key + '->' + str(value) + ', '
        else:
            output+='""->' + str(value) + ', '
    return output
print(letter_occurence(text))
#letter_occurence(text)