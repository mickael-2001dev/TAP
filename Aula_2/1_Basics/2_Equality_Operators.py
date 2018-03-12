# is SAME IDENTITY
# The expression a is b evaluates to True, precisely when identifiers a and b are aliases for the same object.
# is
# is not
# ==
# !=

a = "String A"
b = "String A"

if a is b:
    print("Mesmo: is")

if a == b:
    print("Mesmo: == ")

c = b

if (a is not c):
    print("Diferentes")