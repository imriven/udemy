import json
from difflib import get_close_matches

data = json.load(open("resources/data.json"))

def translate(w):
    w = w.lower()
    # in our data set the words are only lowercase -  we want to make this as user friendly program
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    # The w.title()  will convert the first letter to uppercase and the rest to lowercase. So, if the program didn't find anything for "texas" in the first conditional in lines 6-7 then this conditional will try to search for "Texas". Even if the user entered "TEXAS", this conditional will convert it to "Texas"
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn.lower() == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.lower == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry"
    else:
        return "That word doesn't exist. Please double check it."

word = input("Enter word: ")

output = translate(word)
# print(translate(word))
# we are changing this so that we can get separeate definitions from the dictionary to print out on each line

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)