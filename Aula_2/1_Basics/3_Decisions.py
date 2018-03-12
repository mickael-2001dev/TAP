# IF

done = True

if done:
    print("Ok done")


# else

if not done:
    print("Done")
else:
    print("Not done")

# elif

done2 = False

if not done:
    print("Not done")
elif not done2:
    print("done 2 == True")
else:
    print("Not done")

# ternary operator

price = 900

discount = 10 if price > 1000 else 5
print(discount)





