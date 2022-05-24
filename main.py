# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


# ejena_black
def read_file_content(filename):
    # [assignment] Add your code here 
    """This function reads a textfile and returns it as a string"""
    with open(filename, 'r') as text_file:
        lines = text_file.read()
    text_file.close()
    return lines


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text = text.lower().split()
    word_count = {}
    for word in text:
        count = 1
        if word not in word_count.keys():
            word_count[word] = count
        else:
            word_count[word] += 1
    return word_count