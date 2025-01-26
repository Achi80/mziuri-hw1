def caps_vowels(word):
    vowels = "aeiouy"
    result = ""

    for letter in word:
        if letter.lower() in vowels:
            result += letter.upper()
        else:
            result += letter

    return result


user_word = input("Enter a word: ")

print("Caps Letter:", caps_vowels(user_word))
