TEXT1 = ["The politician who holds the authority of all EU countries has just completely condemned a chunk of the British cabinet wondering aloud",
"What that special place in hell looks like for those who promoted Brexit without even a sketch of a plan how to carry it out safely",
"Sure for a long time the EU has been frustrated with how the UK has approached all of this",
"And sure plenty of voters in the UK are annoyed too at how politicians have been handling these negotiations",
"But it is quite something for Donald Tusk to have gone in like this studs up even though he sometimes reminisces about his time as a football hooligan in his youth"]

TEXT2 = ["An outbreak of the flu in Alabama has closed an elementary and middle school with school officials struggling to find enough healthy teachers to teach",
"The schools will be closed for the rest of the week because of the number of cases of flu among students and employees",
"Lawrence County Schools Superintendent Jon Bret Smith told news outlets that Moulton Elementary School and Moulton Middle School are closed Wednesday through Friday"]


def calculate_fres(total_words, total_sentences, total_syllables):
    """
    Calculate the "Flesch reading-ease score" based on the provided values

    :param total_words: total number of words in a text
    :param total_sentences: total number of sentences in a text
    :param total_syllables: total number of syllables in a text
    :return: "Flesch reading-ease score"
    """
    fres = 206.835 - 1.015 * (total_words / total_sentences) - 84.6 * (total_syllables / total_words)
    return fres


# TEXT1
total_words_text1 = 0
total_sentences_text1 = 0
total_syllables_text1 = 0

# go through each sentence in text 1
for sentence in TEXT1:
    total_sentences_text1 += 1

    # split the sentence to get the dictionary with words
    sentence_words = sentence.split()
    total_words_text1 += len(sentence_words)

    # go through each word in a sentence and count syllables by counting vowels
    for word in sentence_words:
        total_syllables_text1 += word.count('A') + word.count('E') + word.count('I') + word.count(
            'O') + word.count('U') + word.count('a') + word.count('e') + word.count('i') + word.count(
            'o') + word.count('u')

fres_text1 = calculate_fres(total_words_text1, total_sentences_text1, total_syllables_text1)

print("Total words in text 1: {}\n"
      "Total sentences in text 1: {}\n"
      "Total syllables in text 1: {}\n"
      "FRES for text 1: {}\n"
      .format(total_words_text1, total_sentences_text1, total_syllables_text1, fres_text1)
      )

# TEXT2
total_words_text2 = 0
total_sentences_text2 = 0
total_syllables_text2 = 0

# go through each sentence in text 2
for sentence in TEXT2:
    total_sentences_text2 += 1

    # split the sentence to get the dictionary with words
    sentence_words = sentence.split()
    total_words_text2 += len(sentence_words)

    # go through each word in a sentence and count syllables by counting vowels
    for word in sentence_words:
        total_syllables_text2 += word.count('A') + word.count('E') + word.count('I') + word.count(
            'O') + word.count('U') + word.count('a') + word.count('e') + word.count('i') + word.count(
            'o') + word.count('u')

fres_text2 = calculate_fres(total_words_text2, total_sentences_text2, total_syllables_text2)

print("Total words in text 2: {}\n"
      "Total sentences in text 2: {}\n"
      "Total syllables in text 2: {}\n"
      "FRES for text 2: {}"
      .format(total_words_text2, total_sentences_text2, total_syllables_text2, fres_text2)
      )
