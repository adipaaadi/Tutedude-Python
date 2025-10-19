# Assignment-4
# Step 1: Write user input to the file
text_to_write = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text_to_write + "\n")
print("Data successfully written to output.txt.")

# Step 2: Append additional data to the same file
text_to_append = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(text_to_append + "\n")
print("Data successfully appended.")

# Step 3: Read and display the final content of the file
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)

# Task 2: Write, Append, and Read a File
✅ What it does:
Asks the user to enter some text and writes it to a file called output.txt.

Then asks for more text and adds it to the same file.

Finally, it reads and shows the full content of output.txt.
