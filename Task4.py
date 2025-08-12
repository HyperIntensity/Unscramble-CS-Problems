"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


telemarketers = set(call[0] for call in calls)

for i in range(len(calls)):
    if (calls[i][1] in telemarketers):
        telemarketers.discard(calls[i][1])

for i in range(len(texts)):
    if (texts[i][0] in telemarketers):
        telemarketers.discard(texts[i][0])
    elif (texts[i][1] in telemarketers):
        telemarketers.discard(texts[i][1])


print("These numbers coud be telemarketers: ")
for i in sorted(telemarketers):
    print(i)

