import os
import string
from collections import Counter

FILE_NAME = "text.txt"

def count_words(file_content):
    cleaned_content = file_content.lower().translate(str.maketrans('', '', string.punctuation))

    words = cleaned_content.split()

    count = Counter(words)

    for word, number in count.most_common(10):
        print(f'{word}: {number}')

def main():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            file_content = file.read()
        if file_content == '':
            print('File empty, add some text and run again')

        count_words(file_content)
    else:
        with open(FILE_NAME, "w") as file:
            file.write('File created but empty, add some text and run again')
        print('File created but empty, add some text and run again')

if __name__ == "__main__":
    main()