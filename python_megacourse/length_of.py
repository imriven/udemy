your_word = input("Please enter a word you would like to know the length of: ")

def length_of(word):
    return len(word)

characters = length_of(your_word)

print("The length of " +  your_word + " is " + str(characters) + " characters.")