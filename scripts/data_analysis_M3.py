import requests
import matplotlib.pyplot as plt

def extract_answers_sequence(file_path):

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

def generate_means_sequence(collated_answers_path):
    lines = collated_answers_path.splitlines()

    num_questions = 100
    question_answer_groups = [[] for _ in range(num_questions)]

    current_question_index = -1
    question_counter = 0

    
    for line in lines:
        line = line.strip()
        
        if line.startswith("Question"):
            current_question_index = question_counter % num_questions
            question_counter += 1
        
        elif line.startswith("["):
            if "[x]" in line:
                question_answer_groups[current_question_index].append(1)
            else:
                question_answer_groups[current_question_index].append(0)

    
    question_means = [sum(answers) / len(answers) if answers else 0 for answers in question_answer_groups]

    return question_means


url = "https://raw.githubusercontent.com/tdvl3720-uol/Group-Project---Alan-Turing/refs/heads/main/output/collated_answers.txt"
response = requests.get(url)
if response.status_code ==200:
    collated_answers_path = response.text

mean_answer_value = generate_means_sequence(collated_answers_path)
#extract_answers_sequence(collated_answers_path)
print(f"Mean answer values = {mean_answer_value}")                



def visualize_data(collated_answers_path, n):
  
    if n==1:
        x = list(range(1, 101))
        y = mean_answer_value
        plt.scatter(x, y, s=15, marker = '.')
    elif n==2:
        base_url = "https://raw.githubusercontent.com/tdvl3720-uol/Group-Project---Alan-Turing/main/data/"
        file_names = [f"answers_respondent_{i}.txt" for i in range(1, 26)]
        respondent_answers = []

        for file_name in file_names:
            url = base_url + file_name
            response = requests.get(url)
            if response.status_code == 200:
                lines = response.text.splitlines()
                answers = []
                
                for i in range(100):  # There are 100 questions
                    question_answers = lines[i * 4: (i + 1) * 4]  # Get the 4 lines for each question
                    answer = 0
                    
                    for option in question_answers:
                        if "[x]" in option:
                            answer = 1  # Mark the selected option as 1
                            break
                            
                    answers.append(answer)
            respondent_answers.append(answers)  
        else:
            print(f"Failed to load {file_name}")

        plt.figure(figsize=(10, 6))
        for i, answers in enumerate(respondent_answers):
            plt.plot(range(1,101), answers, label = f'Respondent{i+1}')

    else:
        print("error: n=!1, n=!2")
