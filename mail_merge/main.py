#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


draft = ""
names = []

with open("Input/Letters/starting_letter.txt") as letter:
    draft = letter.read()

with open("Input/Names/invited_names.txt") as data:
    new_data = data.readlines()
    for name in new_data:
        names.append(name.strip())

for name in names:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode='w+') as letter:
        new_letter = draft.replace("[name]", name)
        letter.write(new_letter)

print(draft)
print(names)