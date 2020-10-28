# read the file and split the text into tokens
with open("brown.txt", 'r') as file_read:
    text = file_read.read().split(" ")

# create a dictionary with frequencies
freq = {}

for token in text:
    if token.count('-') > 0:
        if token in freq.keys():
            freq[token] += 1
        else:
            freq[token] = 1

# sort the dictionary by decreasing frequency
sorted_data = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# write the data to file
with open("brown_out.txt", 'w') as file_write:
    for token in sorted_data:
        file_write.write("{} \t {} \n" .format(*token))
