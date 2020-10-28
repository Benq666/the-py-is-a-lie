lyrics = "Do you remember 21st night of September ? Love was changing the mind of pretenders While chasing the clouds away Our hearts were ringing In the key that our souls were singing As we danced in the night Remember how the stars stole the night away yeah yeah yeah Hey hey hey Ba de ya say do you remember ? Ba de ya dancing in September Ba de ya never was a cloudy day Ba duda ba duda ba duda badu Ba duda badu ba duda badu Ba duda badu ba duda yeah My thoughts are with you Holding hands with your heart to see you Only blue talk and love Remember how we knew love was here to stay Now December Found the love we shared in September Only blue talk and love Remember the true love we share today Hey hey hey Ba de ya say do you remember ? Ba de ya dancing in September Ba de ya never was a cloudy day There was a Ba de ya say do you remember ? Ba de ya dancing in September Ba de ya golden dreams were shiny days Now our bell was ringing aha Our souls was singing Do you remember every cloudy day yau There was a Ba de ya say do you remember ? Ba de ya dancing in September Ba de ya never was a cloudy day There was a Ba de ya say do you remember ? Ba de ya dancing in September Ba de ya golden dreams were shiny days Ba de ya de ya de ya Ba de ya de ya de ya Ba de ya de ya de ya de ya Ba de ya de ya de ya Ba de ya de ya de ya Ba de ya de ya de ya de ya"

tokens = lyrics.split(" ")
trigrams_list = []
trigrams_list_tuples = []

# create a list of trigrams
while len(tokens) > 2:
    token_1 = tokens.pop(0).lower()
    token_2 = tokens.pop(0).lower()
    token_3 = tokens.pop(0).lower()
    tokens.insert(0, token_3)
    tokens.insert(0, token_2)

    # create a string with tokens separated by underscore
    trigram = token_1 + "_" + token_2 + "_" + token_3
    trigrams_list.append(trigram)

    # create a tuple with three words representing a trigram
    trigram_tuple = (token_1, token_2, token_3)
    trigrams_list_tuples.append(trigram_tuple)

# count frequency
trigrams_frequency = {}
for trigram in trigrams_list:
    if trigram in trigrams_frequency:
        trigrams_frequency[trigram] += 1
    else:
        trigrams_frequency[trigram] = 1

# count tuple frequency
trigrams_frequency_tuples = {}
for trigram in trigrams_list_tuples:
    if trigram in trigrams_frequency_tuples:
        trigrams_frequency_tuples[trigram] += 1
    else:
        trigrams_frequency_tuples[trigram] = 1

# sort the frequencies
sorted_data = sorted(trigrams_frequency.items(), key=lambda x: x[1], reverse=True)
sorted_data_tuples = sorted(trigrams_frequency_tuples.items(), key=lambda x: x[1], reverse=True)

# print the frequencies
print("Tokens.\n"
      "{: <25} {}\n"
      "{: <25} {}" .format("Trigram:", "Frequency:", "-"*10, "-"*10))
for row in sorted_data:
    print("{: <25} {}" .format(*row))

print("\nTuples:\n"
      "{}" .format("-"*10))
for row in sorted_data_tuples:
    print("{}: {}" .format(*row))
