def word_count(text):
    count = 0
    for word in text.split():
        count += 1
    return count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    string_word_count = word_count(file_contents)
    print(string_word_count)

main()