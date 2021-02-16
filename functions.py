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


def args_argument(*args):
    """ *args allows you to enter any number of parameters when calling the function"""
    cnt = 1
    for item in args:
        str_cnt = str(cnt)
        print("Arg " + str_cnt + ": " + str(item))
        cnt += 1

    sumOfVars = sum((args))
    print("Sum of variables =", sumOfVars)
    return sumOfVars


def kwargs_argument(**kwargs):
    """
    key word arguments is a dictionary:
    - kwargs["key1":"val1","key2":val2"]
    To send in values use:
    - function(key1="Val1",key2="val1",key3=int1)
    """
    print("kwargs: {}\n".format(kwargs))
    if "fruit" in kwargs:
        print(" Fruit: {}".format(kwargs["fruit"]))
    if "food" in kwargs:
        print("  Food: {}".format(kwargs["food"]))
    if "num" in kwargs:
        print("Number: {}".format(kwargs["num"]))


def return_boolean(string1):
    return "dog" in string1.lower()


def main():
    no_parameters()

    output = with_parameters(10, 20)
    print("\nwith_parameters override values: ", output)

    output = default_parameters()
    print("\nwith_parameters, provide args  in differen order: ", output)

    output = default_parameters(var2=2, var1=1)
    print("\nwith_parameters, provide args in differen order: ", output)


# main()
# print("return True/False", return_boolean("dog"))
# args_argument(10, 5, 13, 7)
kwargs_argument(fruit="pear", food="pasta", num=44)
