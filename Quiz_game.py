def run_quiz(questions):
    score = 0
    correct_answers = []

    for question in questions:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i + 1}. {option}")

        user_answer = input("Enter your answer (1-4): ")

        if user_answer.isdigit() and int(user_answer) in range(1, 5):
            user_answer = int(user_answer)
            if user_answer == question['answer']:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")

            correct_answers.append(question['answer'])
        else:
            print("Invalid input!")

        print()

    print(f"You scored {score}/{len(questions)}")
    print("Correct answers:")
    for i, answer in enumerate(correct_answers):
        print(f"Question {i + 1}: {questions[i]['options'][answer - 1]}")


questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Paris', 'Rome', 'Madrid', 'London'],
        'answer': 1
    },
    {
        'question': 'What is the largest planet in our solar system?',
        'options': ['Jupiter', 'Saturn', 'Earth', 'Mars'],
        'answer': 1
    },
    {
        'question': 'Who painted the Mona Lisa?',
        'options': ['Leonardo da Vinci', 'Vincent van Gogh', 'Pablo Picasso', 'Michelangelo'],
        'answer': 1
    }
]

run_quiz(questions)
