# Functions

# Define function without params
def no_parameters():
    print("no parameters provided")


# Define function with parameters
def with_parameters(var1, var2):
    ans = var1 + var2
    return ans


# Define function with default values of parameters
def default_parameters(var1=100, var2=200):
    ans = var1 + var2
    return ans


def return_boolean(string1):
    return "dog" in string1.lower()


def main():
    no_parameters()

    output = with_parameters(10, 20)
    print("\nwith_parameters override values: ", output)

    output = default_parameters()
    print("\nwith_parameters, provide args in differen order: ", output)

    output = default_parameters(var2=2, var1=1)
    print("\nwith_parameters, provide args in differen order: ", output)


def pigLatin(word):
    firstletter = word[0]
    extension = "ay"
    vowels = "aeiou"  # Or Use: vowels = ["a", "e", "i", "o", "u"]

    print("first letter:", firstletter, " Remainder of word: ", word[1:])

    if firstletter in vowels:
        print("Word starts with a Vowel")
        return word + extension
    else:
        print("Word starts with a Consonnant")
        return word[1:] + word[0] + extension


translation = pigLatin("apple")
print("Pig Latin Translation is: " + translation)
# main()
# print(return_boolean("dog"))
