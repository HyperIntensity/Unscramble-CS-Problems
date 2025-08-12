## Task 0

**Description**: The problem involves printing out the first record from the texts dataset and the last record of calls from the calls dataset including the time of the text and duration of the call.

**Approach**: I accessed the first element of the given list in texts along with the time and the last record which was the "first last" element in the calls record along with the duration of the call.

**Complexity Analysis**:
- **Algorithm**: No Loops, and a print statment is used to access elements of the list.
- **Big O Notation**: 0(1)
- **Justification**: This problem is a simple lookup which means the statment is independent of the input size. 

--

## Task 1

**Description**: The problem involves sorting both the calls and texts datasets to find the number of distinct numbers.

**Approach**: I ran two loops, one for each dataset, and created a set named 'distinct_numbers' which eliminates duplicates. I then printed out the length of the set.

**Complexity Analysis**:
- **Algorithm**: Two similar for-loops used to itterate and add to a set to eliminate duplicates.
- **Big O Notation**: 0(n)
- **Justification**: This question relies on search which involves a linear relationship with the output. As the inputs (datasets) scale, the time also scales in proportion due to the loops accessing each element in range from 1 to "range(len(dataset))

--

## Task 2

**Description**: The problem involves returning the number that spends the longest time on the phone. Since all dates are from September 2019, no filter needs to be applied.

**Approach**: I isolated the calls dataset and added both the time a number spends as a sender and reciever and added the values to a dictionary.

**Complexity Analysis**:
- **Algorithm**: Uses a singular for loop to read the calls dataset and add the durations.
- **Big O Notation**: 0(n)
- **Justification**: Similar to the last question. This algorithm is linear as the time scales with respect to dataset size as the range is set from 1 to "range(len(dataset))"

--

## Task 3

**Description**: The problem involves analyzing both texts and calls dataset to find people from Bangalore based on area codes. It also asks for a percent of calls made from bangalore to people in Bangalore

**Approach**: I looped through the calls dataset via for loop and looked at the first few characters to see if it matched with area codes. Then I sorted the numbers and printed them accordingly.

**Complexity Analysis**:
- **Algorithm**: Uses a loop to identify area codes to determine if a number is from Bangalore and then added to an array called numbers_called. Then sorts the array and prints out numbers. 
- **Big O Notation**:  0(nlog(n))
- **Justification**: This algorithm is superlinear as the sorting method along with the singular for loop scales the time complexity in a proportion of 0(nlog(n))


## Task 4

**Description**: The problem involves finding a list of telemarketers based on a list of parameters.

**Approach**: I created a telemarketers array with all the numbers from calls. I then used a 2nd and 3rd for loop to check whether the number was a telemarketer based on if they made any texts or recieved any incoming calls.

**Complexity Analysis**:
- **Algorithm**: Uses 3 for loops to itterate and remove any numbers that are not telemarketers.
- **Big O Notation**: 0(nlog(n))
- **Justification**: The question asks to sort the list of telemarketers in lexicographic order with no duplicates so I used a set which is superlinear and hence results in complexity of  0(nlog(n))


