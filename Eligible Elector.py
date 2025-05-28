# Step 1 Ask for the user's age and convert it to an integer
age = int(input("How old are you? "))
# Step 2 Use a conditional to check if the user is eligible
if age >= 18:
    print("Congratulations! 🎉 You are eligible to vote. Go make a difference!")
else:
    yearsLeft = 18 - age # If not eligible yet, calculate how many years are left
    print("Oops! ⏳ You’re not eligible yet. But hey, only " + str(yearsLeft) + " more years to go!")