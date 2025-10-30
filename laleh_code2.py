# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 23:12:34 2024

@author: masou
"""

# Title: Project of Python
#
# Author: Laleh Lellahi 
# Date: 15/04/2024
# ======================================================================================================================

# Importing the required libraries.
import random
import string
from essential_generators import DocumentGenerator


# User defined variables.
NumTestSentences = 4

def main(custom_sentence=None):
    # Activate the document generator.
    GenEngine = DocumentGenerator()

    if custom_sentence != None:
        # If a custom sentence is provided, use it instead of generating random sentences
        sentences = custom_sentence
    else:
        # Generate random sentences
        sentences = [GenEngine.sentence() for _ in range(NumTestSentences)]

    # Loop over the sentences.
    for sentence in sentences:
        print(f'Original sentence is: "{sentence}"')
        # Method 1: reorder all but first and last.
        print(f'\tScramble1: "{reorder_all_but_first_last(sentence)}"')
        # Method 2: reorder first letter.
        print(f'\tScramble2: "{reorder_first_letter(sentence)}"')
        # Method 3: reorder all letter.
        print(f'\tScramble3: "{reorder_all_letters(sentence)}"')
        # Method 4: randomly upper case letters.
        print(f'\tScramble4: "{random_case(sentence)}"')
        print('====' * 1)
        print('\n')

    # Return nothing.
    return
# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================


def reorder_all_but_first_last(sentence):
    """
    Randomly shuffles the middle letters of words in the sentence, while preserving surrounding punctuation.

    Args:
        sentence (str): The input sentence.

    Returns:
        str: The sentence with shuffled middle letters of words.

    Examples:
        reorder_all_but_first_last('This is a sample sentence.')
        'Tihs is a spmlae seecentne.'

    Initiative:
        This function demonstrates the basic functionality of shuffling middle letters while preserving punctuation.
        To go beyond what was covered in class, additional features and techniques could be considered:
        - Incorporate explicit error handling for unexpected input types or edge cases.
        - Implement systematic testing, possibly using a testing library like `unittest` or `pytest`.
        - Explore third-party packages for more advanced text manipulation or analysis.
        - Consider using additional Python features like list comprehensions or advanced slicing.

    """
    # Extract words from the sentence
    words = sentence.split()

    for i in range(len(words)):
        # Extract the punctuations of words
        word_with_punctuation = words[i]
        word = word_with_punctuation.strip(string.punctuation)

        # Checking the length of words
        if len(words[i]) > 3:
            first, *middle, last = word
            random.shuffle(middle)

            # If words with surrounding punctuations
            reconstructed_word = (
                word_with_punctuation[:word_with_punctuation.index(first) + 1] +  # Include the first letter
                ''.join(middle) +
                word_with_punctuation[word_with_punctuation.rindex(last):]  # Include last letter and punctuation
            )

            words[i] = reconstructed_word

    return ' '.join(words)
# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================


def reorder_first_letter(sentence):
    """
    Randomly shuffles the letters of words in the sentence, while preserving surrounding punctuation.

    Args:
        sentence (str): The input sentence.

    Returns:
        str: The sentence with shuffled letters of words, excluding the first letter.

    Examples:
        reorder_first_letter('This is a sample sentence.')
        'hsiT is a epmlas seencetne.'

    Initiative:
        This function demonstrates the basic functionality of shuffling letters while preserving punctuation.
        To go beyond what was covered in class, additional features and techniques could be considered:
        - Incorporate explicit error handling for unexpected input types or edge cases.
        - Implement systematic testing, possibly using a testing library like `unittest` or `pytest`.
        - Explore third-party packages for more advanced text manipulation or analysis.
        - Consider using additional Python features like list comprehensions or advanced slicing.

    """
    # Extract words from the sentence
    
    words = sentence.split()
    for i in range(len(words)):
        word_with_punctuation = words[i]
        word = ''.join(char for char in word_with_punctuation if char not in string.punctuation)

        if len(words[i]) > 1:
            first, *rest = word
            random.shuffle(rest)

            reconstructed_word = (
                word_with_punctuation[:word_with_punctuation.index(first)] +
                ''.join([first] + rest) +
                word_with_punctuation[len(word):]  # Include the rest of the word's punctuation
            )

            words[i] = reconstructed_word

    return ' '.join(words)

# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================


def reorder_all_letters(sentence):
    """
    Randomly shuffles all letters of words in the sentence, while preserving surrounding punctuation.

    Args:
        sentence (str): The input sentence.

    Returns:
        str: The sentence with shuffled letters of words.

    Examples:
        reorder_all_letters('This is a sample sentence.')
        'sTih si a melaps seceennet.'

    Initiative:
        This function demonstrates the basic functionality of shuffling all letters while preserving punctuation.
        To go beyond what was covered in class, additional features and techniques could be considered:
        - Incorporate explicit error handling for unexpected input types or edge cases.
        - Implement systematic testing, possibly using a testing library like `unittest` or `pytest`.
        - Explore third-party packages for more advanced text manipulation or analysis.
        - Consider using additional Python features like list comprehensions or advanced slicing.

    """
    # Extract words from the sentence
    
    words = sentence.split()
    for i in range(len(words)):
        word_with_punctuation = words[i]
        word = ''.join(char for char in word_with_punctuation if char not in string.punctuation)

        if len(words[i]) > 1:
            letters = list(word)
            random.shuffle(letters)

            reconstructed_word = (
                word_with_punctuation[:word_with_punctuation.index(letters[0])] +
                ''.join(letters) +
                word_with_punctuation[len(word):]  # Include the rest of the word's punctuation
            )

            words[i] = reconstructed_word

    return ' '.join(words)

# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================


def random_case(sentence):
    """
    Randomly changes the case of letters in each word of the sentence, while preserving surrounding punctuation.

    Args:
        sentence (str): The input sentence.

    Returns:
        str: The sentence with letters having random cases.

    Examples:
        random_case('This is a sample sentence.')
        'thIS Is A sAmple sEntenCe.'

    Initiative:
        This function demonstrates the basic functionality of randomly changing letter cases while preserving punctuation.
        To go beyond what was covered in class, additional features and techniques could be considered:
        - Incorporate explicit error handling for unexpected input types or edge cases.
        - Implement systematic testing, possibly using a testing library like `unittest` or `pytest`.
        - Explore third-party packages for more advanced text manipulation or analysis.
        - Consider using additional Python features like list comprehensions or advanced slicing.

    """
    # Extract words from the sentence
    words = sentence.split()

    for i in range(len(words)):
        # Extract the punctuations of words
        word_with_punctuation = words[i]
        word = word_with_punctuation.strip(string.punctuation)

        # Checking the length of words
        if len(words[i]) > 1:
            modified_word = ''.join([
                random.choice([char.lower(), char.upper()]) for char in word
            ])

            # If words with surrounding punctuations
            reconstructed_word = (
                word_with_punctuation[:word_with_punctuation.index(word[0])] +  # Exclude the first letter
                modified_word +
                word_with_punctuation[word_with_punctuation.rindex(word[-1]) + 1:]  # Include last letter and punctuation
            )

            words[i] = reconstructed_word

    return ' '.join(words)
# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================


if __name__ == '__main__':
    # a custom sentence as an argument to the main function
    custom_sentence = ["hello... can you handle???!!! punctuation??!!"]
    main(custom_sentence)
    