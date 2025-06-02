import pandas as pd

def student_score_tracker():
    # Initialize empty dictionary to store data
    students = {'Name': [], 'Score': []}
    
    print("\nSTUDENT SCORE TRACKER")
    print("---------------------")
    
    # Input loop
    while True:
        try:
            name = input("Enter student name (or 'done' to finish): ")
            if name.lower() == 'done':
                break
                
            score = float(input("Enter student score: "))
            if score < 0 or score > 100:
                raise ValueError("Score must be 0-100")
                
            students['Name'].append(name)
            students['Score'].append(score)
            
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    
    # Create DataFrame and analyze
    if students['Name']:
        df = pd.DataFrame(students)
        
        print("\n===== RESULTS =====")
        print(df)
        print("\nSTATISTICS:")
        print(f"Average score: {df['Score'].mean():.2f}")
        print(f"Highest score: {df['Score'].max()}")
        print(f"Lowest score:  {df['Score'].min()}")
        
        # Save to file
        try:
            df.to_csv('student_scores.txt', sep='\t', index=False)
            print("\nData saved to 'student_scores.txt'")
        except IOError:
            print("Error: Could not save file")
    else:
        print("No student data entered.")

# Run the program
student_score_tracker()