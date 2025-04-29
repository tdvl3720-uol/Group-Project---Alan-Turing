def extract_answers_sequence(file_path):
    """
    Parses the respondent’s answers into a structured sequence.

    Input: path (str) to a quiz answers text file.

    Parameters:
        file_path (str): The path to the respondent's text file.

    Output: List of 100 integers, where each number is 1, 2, 3, 4 (corresponding to the
    answer marked by the respondent), or 0 (if the question was not answered).

    """

    answers = []
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines() if line.strip() != ""]

    for i in range(0, len(lines), 5):
        question_block = lines[i:i+5]
        selected = 0
        for j in range(1, 5):
            if "[x]" in question_block[j]:
                selected = j
        answers.append(selected)

    return answers


def write_answers_sequence(answers, respondent_id):
    """
    Input: List of 100 integers (answer sequence) and an integer n (respondent ID).
    Output: Writes the sequence to a text file named answers_list_respondent_n.txt.
    Purpose: Save the extracted sequence for further use.
    """
    file_name = f"answers_list_respondent_{respondent_id}.txt"
    with open(file_name, "w") as file:
        file.write(", ".join(map(str, answers)))