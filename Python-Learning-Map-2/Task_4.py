# Exercise 1

def count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0


filename = 'sample.txt'  
word_count = count_words(filename)
print(f"The file contains {word_count} words.")


# Exercise 2

def log_message(message, logfile='app.log'):
    try:
        with open(logfile, 'a') as file:
            file.write(f"{message}\n")
        print("Message logged successfully.")
    except IOError:
        print("Error: Could not write to log file.")

# Example usage
log_message("Application started")
log_message("User logged in")
log_message("Error occurred", "error.log")