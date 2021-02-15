def pigLatin(word=False, debugging=False):
    """
    Purpose:
        Translate word into piglatin

    Usage:
        pigLatin(<enter word>)
        pigLatin()

    Output:
        Return 'translation' & Print translation to STDOUT

    Created By: MichaelLean, 210216
    """
    if not word:
        word = input("Word to Translate? ")

    firstletter = word[0]
    extension = "ay"
    vowels = "aeiou"  # Or Use: vowels = ["a", "e", "i", "o", "u"]

    if debugging:
        print("first letter:", firstletter, " Remainder of word: ", word[1:])

    if firstletter in vowels:
        if debugging:
            print("Word starts with a Vowel")
        translation = word + extension
    else:
        if debugging:
            print("Word starts with a Consonnant")
        translation = word[1:] + word[0] + extension

    print("\nPig Latin Translation is: " + translation)
    return translation


translation = pigLatin("word")
