#exercise 1

def word_frequency(sentence):
    word_count = {}
    words = sentence.split()
    
    for word in words:
        cleaned_word = word.strip('.,!?').lower() # Remove punctuation and convert to lowercase
        if cleaned_word:
            word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1
    
    return word_count

sentence = "Hello world! Hello Python. Python is cool, isn't it?"
frequency = word_frequency(sentence)
print("Word frequencies:")
for word, count in frequency.items():
    print(f"{word}: {count}")


#exercise 2

def reverse_string(input_str):
    return input_str[::-1]

# Get user input and reverse it
user_input = input("Enter a string to reverse: ")
reversed_str = reverse_string(user_input)
print(f"Reversed string: {reversed_str}")