import  json
#help(json.load)
from difflib import get_close_matches
data = json.load(open("data.json"))
#print(data)
#word = input("enter word: ")
word = "rain"


def dict(word=""):
    word = word.lower()
    if word in data:
        return data[word]
   # elif len(get_close_matches(word,data.keys())) >0:
    #    return get_close_matches(word,data.keys())[0]
       # if yn == "Y":
        #    return data[get_close_matches(word,data.keys())[0]]
        #elif yn == "N":
         #   return "The word doesn't exist . Please double check it."
        #else:
         #   return "Your entry is didn't recognized ."
    #else:
     #   return "The word doesn't exist . Please double check it."
     

#output = dict(word)

#if type(output) == list:
 #   for item in output:
  #      print(item)
#else:
   # print(output)
