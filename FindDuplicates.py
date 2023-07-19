import re


def findDuplicates(sentence):
    # Define a regular expression pattern to match all punctuation
    punctuation_pattern = r"[^\w\s]"

    # Use the re.sub() function to replace all occurrences of punctuation with an empty string
    sentence = re.sub(punctuation_pattern, "", sentence)

    # Convert the sentence to lowercase
    sentence = sentence.lower()

    # Split the sentence into words
    words = sentence.split()

    # Create an empty dictionary to store the frequency of each word
    word_freq = {}

    # Iterate through each word in the sentence
    for word in words:
        # If the word is already in the dictionary, increment its frequency
        if word in word_freq:
            word_freq[word] += 1
        else:
            # If the word is not in the dictionary, add it with a frequency of 1
            word_freq[word] = 1

    # Create a list to store the duplicate words
    duplicates = []

    # Iterate through the dictionary and find the words with frequency greater than 1
    for word, frequency in word_freq.items():
        if frequency > 1:
            duplicates.append(word)

    return duplicates


# Test the function
sentence = (
    "The quick brown fox jumps over the lazy dog. The quick fox jumps over the dog."
)
result = findDuplicates(sentence)
print("Duplicates:", result)
