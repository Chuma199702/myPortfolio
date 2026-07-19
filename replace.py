# PSEUDOCODE:
# 1. Store the sentence "The!quick!brown!fox!jumps!over!the!lazy!dog." in a variable
# 2. Replace all "!" with spaces using the replace() function
# 3. Print the updated sentence
# 4. Convert the sentence to uppercase using upper()
# 5. Print the uppercase sentence
# 6. Reverse the sentence using slicing
# 7. Print the reversed sentence

# Step 1: Store the original sentence
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Step 2: Replace "!" with spaces
new_sentence = sentence.replace("!", " ")

# Step 3: Print the updated sentence
print(new_sentence)

# Step 4: Convert to uppercase
upper_sentence = new_sentence.upper()

# Step 5: Print the uppercase sentence
print(upper_sentence)

# Step 6: Reverse the sentence using slicing
reversed_sentence = new_sentence[::-1]

# Step 7: Print the reversed sentence
print(reversed_sentence)