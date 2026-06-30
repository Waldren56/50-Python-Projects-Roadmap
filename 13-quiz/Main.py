import sys

def show_results(correct_answers, total_questions, wrong_answers):
    if correct_answers == total_questions:
        print('\nYou have answered everything correctly!')
    else:
        if correct_answers < 1:
            print('\nNo correct answer.')
        else:
            print(f'\n{correct_answers} correct answer' if correct_answers == 1
                  else f'\n{correct_answers} correct answers')

        while True:
            see_wrong_choices = input('Would you like to see what answer you did wrong? (y/n): ')
            if see_wrong_choices not in ['y', 'n']:
                print('Please enter either "y" or "n".')
                continue
            else:
                if see_wrong_choices == 'y':
                    for i in range(len(wrong_answers)):
                        print(
                            f'\n{i + 1}: {wrong_answers[i]["Question"]}\n'
                            f'   The answers were: {wrong_answers[i]["Answers"]}\n'
                            f'   You answered: {wrong_answers[i]["User Answer"]}\n'
                            f'   Correct answer: {wrong_answers[i]["Correct Answer"]}'
                        )
                else:
                    print()
                    sys.exit('Thanks for playing!')
                break

def display_questions():
    questions = [
        {
            'Question': 'What is the capital of Italy?',
            'Answers': ['Milan', 'Rome', 'Naples', 'Turin'],
            'Correct Answer': 2
        },
        {
            'Question': 'What is 15 x 3',
            'Answers': ['35', '40', '45', '60'],
            'Correct Answer': 3
        },
        {
            'Question': 'What happened in 1914',
            'Answers': ['WW1', 'WW2', 'WW3', 'WW4'],
            'Correct Answer': 1
        }
    ]

    return questions

def manage_answer(question):
    while True:
        try:
            user_answer = int(input(f'\nEnter your answer (1-{len(question["Answers"])}): > '))
            if not 1 <= user_answer <= len(question['Answers']):
                print('Please enter a valid answer.')
                continue
            else:
                break
        except ValueError:
            print('Please enter an integer.')

    return user_answer

def main():
    correct_answers = 0
    total_questions = 0
    wrong_answers = []

    questions = display_questions()

    for question in questions:
        print('\n\n' + question['Question'])
        for i, answer in enumerate(question['Answers'], start=1):
            print(f'{i}: {answer}')

        user_answer = manage_answer(question)

        if user_answer != question['Correct Answer']:
            print('Wrong answer.')

            wrong_answers.append({
                "Question": question["Question"],
                "Answers": question["Answers"],
                "User Answer": user_answer,
                "Correct Answer": question["Correct Answer"]
            })
        else:
            print('Correct answer.')
            correct_answers += 1
        total_questions += 1

    show_results(correct_answers, total_questions, wrong_answers)

if __name__ == '__main__':
    main()