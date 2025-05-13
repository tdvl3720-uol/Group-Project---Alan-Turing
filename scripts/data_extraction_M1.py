def extract_answers_sequence(file_path):
    """
    Extracts a list of 100 answers from the given quiz answer file, 
    and parses the respondent’s answers into a structured sequence.
    
    Input: path (str) to a quiz answers text file.

    Output: List of 100 integers, where each number is 1, 2, 3, 4 (corresponding to the
    answer marked by the respondent), or 0 (if the question was not answered).

    """

    answers = []
    with open(file_path, "r") as file:
        lines = file.readlines()

#Removing empty lines from the file

    clean_lines = []
    for line in lines:
        line = line.strip()
        if line != "":
            clean_lines.append(line)

#Adding the chosen answer to the answer List. 1 question is 5 lines  

    for i in range(0, len(clean_lines), 5):
        question_block = clean_lines[i:i+5]
        chosen_answer = 0
        for option in range(1, 5):
            if "[x]" in question_block[option]:
                chosen_answer = option
        answers.append(chosen_answer)

    return answers

def write_answers_sequence(answers, respondent_id):
    """
    Save the extracted sequence for further use.

    Input: List of 100 integers (answer sequence) and an integer n (respondent ID).

    Output: Writes the sequence to a text file named answers_list_respondent_n.txt.

    """
    with open(file_name, "w") as file:
        for i in range(len(answers)):
            file.write(str(answers[i]))
            if i < len(answers) - 1:
                file.write(", ")

