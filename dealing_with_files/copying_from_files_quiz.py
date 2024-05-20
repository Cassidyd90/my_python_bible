"""
Example quiz program
Get Quiz Questions from one file
Get user Answers 
Put user quiz score in new file
"""

quiz_questions_txt = r"C:\Development\my_python_bible\dealing_with_files\quiz_questions.txt"
quiz_results_txt = r"C:\Development\my_python_bible\dealing_with_files\quiz_results.txt"

quiz_questions_read = open(quiz_questions_txt, 'r')
quiz_list = quiz_questions_read.read().splitlines()
quiz_dict = {x.split('=')[0] + "=" : x.split('=')[1] for x in quiz_list}
quiz_questions_read.close()


user_answers = {}
"""
Loop through dictionary to print question then get response
"""
for question, answer in quiz_dict.items():
    question_prompt = question 

    print(question)

    user_input = input("What's the answer?")

    user_answers[question] = user_input


questions_set = set(quiz_dict.items())
answers_set = set(user_answers.items())

results = {len(answers_set.intersection(questions_set)): len(questions_set)}


my_file_writing = open(quiz_results_txt, 'w') 
for result, total in results.items():
    my_file_writing.write(f"Your final score is {result}/{total}")
my_file_writing.close()


