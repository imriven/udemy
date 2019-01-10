import json
from difflib import get_close_matches

data = json.load(open("resources/data.json"))

def ask_match(word):

    ask_word =  input("Did you mean %s instead? Please type Y or N: " % word)
    if ask_word.lower() == "y":
        return True
    elif ask_word.lower() == "n":
        return False
    else:
        return "Please try again"   

def translate(w):
    w = w.lower()
    # in our data set the words are only lowercase -  we want to make this as user friendly program
    if w in data:
        return data[w]

    closest_matches = get_close_matches(w, data.keys())
    if len(closest_matches) > 0:
        for match in closest_matches:
            if ask_match(match):
                return data[match]
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

print(translate(word))