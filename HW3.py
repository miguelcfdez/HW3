import requests
def download_book(url):
    """
    download a book given a url
    :param url: the url containing the book
    :return: None
    """
    print(url)
    response = requests.get(url)
    print(response.status_code)
    with open('book.txt', 'w') as f:
        f.write(response.text)

# download_book("https://www.gutenberg.org/cache/epub/1342/pg1342.txt")

#def download_book(url):
    #"""
    #download a book given a url
    #:param url: the url containing the book
    #:return: None
    #"""
    #print(url)
    #response = requests.get(url)
    #print(response.status_code)
    #with open('book2.txt', 'w') as f:
    #    f.write(response.text)

# download_book("https://www.gutenberg.org/cache/epub/1513/pg1513.txt")

punctuation = ",.;:!?\"'()[]{}-*<>_/\\|@#$%^&~`“”"

def count_unique_words(file_name):
    """
    Counts how many unique words appear in a text file
    :param file_name: name of the text file
    :return: number of unique words
    """
    try:
        fd = open(file_name, "r", encoding="utf-8")
    except:
        print("Error opening file:", file_name)
        return 0
    words_dict = {}
    for line in fd:
        for p in punctuation: ### We remove punctuation
            line = line.replace(p, " ")
        line = line.lower() ### Convert to lowercase
        words = line.split() ### Split into words
        for word in words: ### Add words to dictionary
            if word not in words_dict:
                words_dict[word] = 1
            else:
                words_dict[word] += 1
    fd.close()
    return len(words_dict)

book1 = "book.txt"      # Pride and Prejudice
book2 = "book2.txt"     # Romeo and Juliet

unique1 = count_unique_words(book1)
unique2 = count_unique_words(book2)

print("Unique words in book1:", unique1)
print("Unique words in book2:", unique2)

if unique1 > unique2:
    print("Book 1 has more unique words.")
elif unique2 > unique1:
    print("Book 2 has more unique words.")
else:
    print("Both authors used the same number of unique words.")

