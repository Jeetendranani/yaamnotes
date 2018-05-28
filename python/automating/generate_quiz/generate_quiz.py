#! python3
# random quiz generator - create quizzes with questions and answers in random oder, along with the answer key.


import random


# The quiz data. keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# generate 35 quiz files.
for quiz_num in range(35):
    # create teh quiz and answer key files.
    quiz_file = open('captitalquiz{}s.txt'.format(quiz_num+1), 'w')
    answer_file = open('capitalquiz_anwser{}s.txt'.format(quiz_num+1), 'w')

    # write out the header to the quiz.
    quiz_file.write('Name: \n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + 'State Capital Quiz (Form {}'.format(quiz_num+1))
    quiz_file.write('\n\n')

    # shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # loop through all 50 states, making a question for each.
    for question_num in range(50):

        # Getright and wrong ansers.
        correct_answer = capitals[states[question_num]]
        wrong_answer = list(capitals.values())
        del wrong_answer[wrong_answer.index(correct_answer)]
        wrong_answer = random.sample(wrong_answer, 3)
        answer_options = wrong_answer + [correct_answer]
        random.shuffle(answer_options)

        # write the question and answer options to the quiz file.
        quiz_file.write('{}. What is the capital of {}?\n'.format(question_num+1, states[question_num]))
        for i in range(4):
            quiz_file.write('    {}. {}\n'.format('ABCD'[i], answer_options[i]))
        quiz_file.write('\n')

        # write the answer key to a file
        answer_file.write('{}. {}\n'.format(question_num+1, 'ABCD'[answer_options.index(correct_answer)]))
    quiz_file.close()
    answer_file.close()
