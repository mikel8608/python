'''
  Global Vars
  Input Vars

'''

#
# Global Variable...this is actually a local variable that has scope accross all code in this script
#
x = 1
print("Original Value of x: ", x)


def update_global_var():
    # Set x as global here to force the global value to be updated.
    global x
    x += 1
    print("inside function 'update_global_var': ", x)

update_global_var()
print("outside function after updating value in 'update_global_var': ", x)

# Preferred method to update a global var is to assign it the output of a function.
def update_global_var_perferred_method():
    x = 3
    print("inside function 'update_global_var_perferred_method': ", x)

    val = 4
    return val


x = update_global_var_perferred_method()
print(
    "outside function after updating value in 'update_global_var_perferred_method': ", x
)

print('\n')
print("Use the value of 'None' as a place holder for empty vars. It is also the DEFAULT Return value for functions.")
b = None
print(b)

print("\nUse Booleans as 'True' & 'False'. This is case sensitive")
