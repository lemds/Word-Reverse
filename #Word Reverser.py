# Word Reverser
def reverse_word():
    print("Welcome to the Word Reverser!")
    word = input("Enter a word or sentence to reverse: ")
    
    # Reverse the input
    reversed_word = word[::-1]
    
    print(f"The reversed word/sentence is: {reversed_word}")

# Run the reverser
reverse_word()

