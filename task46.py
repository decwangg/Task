# Step 1: Declare a variable to store the user's input
user_number = int(input("Enter a name to calculate its factoral:"))

#Step 2: Initialoze the factoral variable
factoral = 1
# Step 3: Use a while loop to calculate the factoral
i = 1
while i<= user_number:
    factoral *=i
    i += 1
# Step 4: Display the factoral
print(f'The factoral of{user_number}is {factoral}')
