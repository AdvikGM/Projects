word = input("Enter the word: ")

found = False

for letter in word:
    if letter == "a":
        print("Found A")
        found = True

if found == False:
    print("Did not find A")
