def read_file_contents(file_name):
    with open(file_name, 'r') as readable_file:
        return [line.strip() for line in readable_file.readlines()]


def get_final_score_message(number_of_questions, number_of_correct_answers):
    return f"Your final score is {number_of_correct_answers}/{number_of_questions}."


def write_contents_to_file(file_name, contents_to_write):
    with open(file_name, 'w') as writable_file:
        writable_file.write(contents_to_write)


def run_quiz_program(file_name):
    correct_answer_counter = 0
    file_list = read_file_contents(file_name)

    for line in file_list:
        question, answer = line.split("=")
        user_answer = input(question + "=")
        if user_answer == answer:
            correct_answer_counter += 1

    final_result = get_final_score_message(len(file_list), correct_answer_counter)
    print(final_result)
    write_contents_to_file('result.txt', final_result)


run_quiz_program('questions.txt')
