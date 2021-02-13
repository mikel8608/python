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


def main():
    no_parameters()

    output = with_parameters(10, 20)
    print("\nwith_parameters override values: ", output)

    output = default_parameters()
    print("\nwith_parameters, provide args in differen order: ", output)

    output = default_parameters(var2=2, var1=1)
    print("\nwith_parameters, provide args in differen order: ", output)


main()