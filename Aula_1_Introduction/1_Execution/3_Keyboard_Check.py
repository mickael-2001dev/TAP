done = True
while done:
    name = input("Enter yor name:")
    if name == '':
        done = False
        print("Exit.")
    else:
        print(name)

