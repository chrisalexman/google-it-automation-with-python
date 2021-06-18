import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we",
                           "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was",
                           "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by",
                           "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more",
                           "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    frequencies = {}
    without_punctuation = ""

    for line in file_contents:
        for char in line:
            if char.isalpha() or char == " ":
                without_punctuation += char.lower()

    after_split = without_punctuation.split()

    # print(after_split)

    for word in after_split:
        if word not in uninteresting_words:
            if word.lower() not in frequencies:
                frequencies[word.lower()] = 1
            else:
                frequencies[word.lower()] += 1

    # print(frequencies)

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    cloud.to_file("myfile.jpg")
    return cloud.to_array()


# Display your wordcloud image

file_contents = open("/home/chris/PycharmProjects/"
                     "Google-IT-Automation-with-Python/Crash Course in Python/Week_6/input.txt", "r")

my_image = calculate_frequencies(file_contents)
plt.imshow(my_image, interpolation='nearest')
plt.axis('off')
plt.show()

file_contents.close()
