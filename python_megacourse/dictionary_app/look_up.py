# create a function that uses the input as the key and then returns the value for that key. try to incorporate loading of JSON file and print the output
import json

def look_up_word(word, path):
    word_dictionary = open(path, "r")
    content_dict = json.load(word_dictionary)
    if word in content_dict:
        print(content_dict[word])

look_up = input("What word would you like to look up?: ")
look_up_word(look_up, "resources/data.json")
