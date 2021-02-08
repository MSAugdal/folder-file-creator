from pathlib import Path


def folder_file_creator(folder_name, file_name):
    path = r"F:\OneDrive\Skrivebord"

    directory = Path(path) / folder_name
    directory.mkdir()

    complete_file = Path.joinpath(directory, file_name+".py")
    with open(complete_file, "w") as file:
        file.writelines("#auto created file")


folder_file_creator(folder_name="your_folder_name", file_name="your_file_name")
