def word_count(text):
    count = 0
    for word in text.split():
        count += 1
    return count

def character_count(text):
    character_count_dict = {}
    for word in text.split():
        for character in word:
            character = character.lower()
            if character in character_count_dict:
                character_count_dict[character] += 1
            else:
                character_count_dict[character] = 1
    return character_count_dict


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    string_word_count = word_count(file_contents)
    print(string_word_count)
    character_count_dict = character_count(file_contents)
    print(character_count_dict)

main()