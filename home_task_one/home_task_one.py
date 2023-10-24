"""
TASK:
Word Frequency Counter

You are given a text file containing a large amount of text. Your task is to create a program that reads the file,
counts the frequency of each word, and displays the top N most frequent words along with their counts.

Instructions:
1. Read the contents of the text file into a string variable.
2. Create a generator function that yields each word from the string one at a time. Remove any punctuation marks or
    special characters from the words.
3. Use a defaultdict from the collections module to count the frequency of each word. The word should be used as the
    key, and the count should be the value.
4. Iterate through the words generated by the generator and update the frequency counts in the defaultdict.
5. Implement a function that takes the frequency counts and a number N as arguments and returns the top N most frequent
    words as a list of tuples (word, count), sorted in descending order by count.
6. Test your program by providing a text file and displaying the top N most frequent words, where N is a number of your
    choice.
"""

import string
from collections import defaultdict


def read_file(file_name: str):
    """
    Reads the content of a file and returns it as a string.
    Args:
        file_name (str): The name (and path, if required) of the file to be read.
    Returns:
        str: The content of the file as a string.
    """
    with open(file_name, 'r') as file:
        return file.read()


def word_generator(text: str):
    """
    Generates words from a given text, removing punctuation marks.
    Args:
        text (str): The input text string.
    Yields:
        str: A cleaned, lowercased word from the input text.
    """
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)

    for word in cleaned_text.split():
        yield word.lower()


def word_frequency(text):
    """
    Computes the frequency of each word in the input text.
    Args:
        text (str): The input text string.
    Returns:
        dict: A dictionary containing the word frequencies, with the structure (word, number of mentions).
    """
    word_count = defaultdict(int)
    generator = word_generator(text)

    for word in generator:
        word_count[word] += 1

    return word_count


def get_most_frequent_words(text: str, top_: int) -> list[tuple]:
    """
    Returns the top N most frequent words as a list of tuples (word, count).
    Args:
        text (str): The input text string.
        top_ (int): The number of top frequent words to return.
    Returns:
        list[tuple]: A list of tuples (word, count), representing the top N most frequent words in descending order.
    """
    words_count = word_frequency(text)
    # key parameter determines which element of the tuple should be used for sorting.
    return sorted(words_count.items(), key=lambda element: element[1], reverse=True)[:top_]


if __name__ == '__main__':
    file_name = 'karpathy-pod.txt'
    file_content = read_file(file_name)

    top_n_words = get_most_frequent_words(file_content, 5)
    print(top_n_words)