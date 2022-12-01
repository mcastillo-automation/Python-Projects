import re

pattern = "\Wname\W"

# Grab invited_names.txt and store lines as a list.
with open('./Names/invited_names.txt', mode='r') as file:
    names = file.read().splitlines()

# Read starting_letter.txt and store it as template
with open('./Input/Letters/starting_letter.txt', mode='r') as file:
    template = file.read()

# Iterate through names list and use re.sub() to replace [names] with list values.
for items in names:
    with open(f'./Output/ReadyToSend/{items}.txt', mode='w+') as text:
        text.write(re.sub(pattern, repl=items, string=template))
