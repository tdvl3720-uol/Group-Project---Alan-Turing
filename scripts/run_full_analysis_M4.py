import requests
from pathlib import Path
import os 
import matplotlib.pyplot as plt
import numpy as np

def download_answer_files(cloud_url:str, path_to_data_folder: str, respondent_index:int):
   for i in range(1, respondent_index+1):
        file_name= f"answers_respondent_{i}.txt"
        file_url=f"{cloud_url}/{file_name}?raw=true"
        local_name = os.path.join(path_to_data_folder, file_name)
        try:
                    response = requests.get(file_url)
                    response.raise_for_status()
                    with open(local_name, "w", encoding="utf-8") as file:
                        file.write(response.text)
                    print(f"Downloaded: {file_name}")
        except requests.RequestException as e:
            print(f"Failed to download {file_name}: {e}")
          
download_answer_files(
    cloud_url="https://github.com/tdvl3720-uol/Group-Project---Alan-Turing/raw/main/data",
    path_to_data_folder="data",
    respondent_index=25)


def collate_answer_files(data_folder_path):
    output_file_path="output/collated_answers.txt"
    
    files = sorted(os.listdir(data_folder_path))
    
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        for filename in files:
            file_path = os.path.join(data_folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as infile:
                content = infile.read()
                outfile.write(content)
                outfile.write("\n*\n")  
    print(f"Collated answers saved to {output_file_path}")

def extract_answers_sequence(file_path):

    answers = []
    with open(file_path, "r") as file:
        lines = file.readlines()

    clean_lines = []
    for line in lines:
        line = line.strip()
        if line != "":
            clean_lines.append(line)

    for i in range(0, len(clean_lines), 5):
        question_block = clean_lines[i:i+5]
        chosen_answer = 0
        for option in range(1, 5):
            if "[x]" in question_block[option]:
                chosen_answer = option
        answers.append(chosen_answer)

    return answers

def generate_means_sequence(collated_answers_path):

    answers = extract_answers_sequence(collated_answers_path)
    means = []
    num_questions = 100
    num_respondents = len(answers)//num_questions
    for i in range(num_questions):
        total = 0 
        count = 0

        for j in range(num_respondents):
            index = j * num_questions + i
            value = answers[index]
            if value != 0: # to ignore missing answers marked as '0'
                total += value
                count += 1
        mean = total / count if count > 0 else 0
        means.append(mean)
    return means

collated_answers_path = "output/collated_answers.txt"
means = (generate_means_sequence(collated_answers_path))
print(means)

def visualize_data(collated_answers_path, n):
  
    if n==1:
        x = list(range(1, 101))
        y = means
        plt.scatter(x, y, s=15, marker = '.')
        plt.xlabel("Question number")
        plt.ylabel("Mean value")
        plt.title("Means sequence")

    elif n==2:
        base_url = "https://raw.githubusercontent.com/tdvl3720-uol/Group-Project---Alan-Turing/main/data/"
        file_names = [f"answers_respondent_{i}.txt" for i in range(1, 26)]
        respondent_answers = []

        for file_name in file_names:
            url = base_url + file_name  # builds the url to fetch each file
            response = requests.get(url)
            if response.status_code == 200:
                lines = response.text.splitlines()
                answers = []
                
                for i in range(100):  
                    question_answers = lines[i * 4: (i + 1) * 4]  # slices 4 lines for the answer options for each question
                    answer = 0
                    
                    for option in question_answers:
                        if "[x]" in option:
                            answer = 1  
                            break
                            
                    answers.append(answer)
                respondent_answers.append(answers)  
            else:
                print(f"Failed to load {file_name}")

        plt.figure(figsize=(10, 6))
        for i, answers in enumerate(respondent_answers):
            plt.plot(range(1,101), answers, label = f'Respondent_{i+1}')
            plt.xlabel("Question numbers")
            plt.ylabel("Answered(1) / Not Answered(0)")
            plt.title("Individual Answers")
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title="Respondents")
            plt.xticks(np.arange(0, 101, 10))

    else:
        print("error: n!=1, n!=2")

visualize_data(collated_answers_path, 1)
visualize_data(collated_answers_path, 2)


