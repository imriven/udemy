import json
from difflib import get_close_matches

data = json.load(open("resources/data.json"))

def translate(w):
    w = w.lower()
    # in our data set the words are only lowercase -  we want to make this as user friendly program
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
      #  return "Did you mean %s instead?" % get_close_matches(w, data.keys())[0]
        ask_word =  input("Did you mean %s instead? Please type Y or N: " % get_close_matches(w, data.keys())[0])
        correct_word = get_close_matches(w, data.keys())[0]
        if ask_word == "Y":
            return  correct_word
        elif ask_word == "N":
            return "Your word wasn't found. Try again."
        else:
            return "Please"
            
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

print(translate(word))