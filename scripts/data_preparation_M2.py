def download_answer_files(cloud_url: str, path_to_data_folder: str, respondent_index: int):
    if not os.path.exists(path_to_data_folder):
        os.makedirs(path_to_data_folder)

    for i in range(1, respondent_index + 1):
        file_name = f"answers_respondent_{i}.txt"
        file_url = f"{cloud_url}/{file_name}?raw=true"
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
    respondent_index=40
)

