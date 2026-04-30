word = input("Enter the word: ")

found = False

for letter in word:
    if letter == "e":
        print("Found E")
        found = True

if found == False:
    print("Did not find E")
