import os
from collections import Counter

FILE_NAME = "text.txt"

def count_words(file_content):
    parole = file_content.split()

    count = Counter(parole)

    for word, number in count.most_common(10):
        print(f'{word}: {number}')

def main():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            file_content = file.read()

        count_words(file_content)
    else:
        with open(FILE_NAME, "w") as file:
            file.write('File created but empty, add some text and run again')
        print('File created but empty, add some text and run again')

if __name__ == "__main__":
    main()