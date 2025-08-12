"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
#All timestamps are from 2016 and September
from collections import defaultdict


total_duration = defaultdict(int)

for i in calls:
    caller = i[0]
    reciever = i[1]
    duration = int(i[3])

    total_duration[caller] += duration
    total_duration[reciever] += duration

print(str(max(total_duration, key=total_duration.get)) + " spent the longest time, " + str(total_duration[max(total_duration, key=total_duration.get)]) + " seconds, on the phone during September 2016.")

