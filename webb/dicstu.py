import  json
#help(json.load)
from difflib import get_close_matches
data = json.load(open("data.json"))
#print(data)
word = ""



def dicty(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) >0:
        return data[get_close_matches(word,data.keys())[0]]
        

output1 = dicty(word)

if type(output1) == list:
    for item in output1:
        print(item)
else:
    print(output1)

