import random

def run_quiz(questions):

    # Shuffle the question
    random.shuffle(questions)

    score = 0
    for q in questions:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")
        answer = input("Your answer (1/2/3/4): ")
        if answer == str(q["answer"]):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {q['options'][q['answer'] - 1]}")
    print(f"\nYour final score: {score}/{len(questions)}")

# Quiz questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Madrid"],
        "answer": 3
    },
    {
        "question": "What is 5 * 6?",
        "options": ["11", "30", "20", "60"],
        "answer": 2
    },
    {
        "question": "Which language is used for web development?",
        "options": ["Python", "HTML", "C++", "Java"],
        "answer": 2
    },
    {
        "question": "What planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": 2
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["Mark Twain", "Jane Austen", "William Shakespeare", "Charles Dickens"],
        "answer": 3
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "answer": 2
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Oxygen", "Gold", "Silver", "Iron"],
        "answer": 1
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["5", "6", "7", "8"],
        "answer": 3
    }
]


# Run the quiz
run_quiz(quiz_questions)
