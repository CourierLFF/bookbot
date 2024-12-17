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
    character_count_dict = dict(sorted(character_count_dict.items(), key=lambda item: item[1], reverse=True))
    return character_count_dict

def report_generator(word_count_number, character_count_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count_number} words found in the document")
    print("\n")
    for item in character_count_dict:
        print(f"The '{item}' character was found {character_count_dict[item]} times")
    print("--- End report ---")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    string_word_count = word_count(file_contents)
    character_count_dict = character_count(file_contents)
    report_generator(string_word_count, character_count_dict)

main()