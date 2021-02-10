import os


class FolderFileCreator:
    parent_dir = r"F:\OneDrive\Skrivebord"
    directory = input("what do you want your directory to be called: ").strip().title()
    dir_path = os.path.join(parent_dir, directory)
    os.mkdir(dir_path)

    file_type = input("what file type do you want your file to be: ").replace(" ", "").strip().lower()
    file = input(
        "what do you want your file to be called: ").replace(" ", "").strip().title()
    file_path = os.path.join(dir_path, file)
    with open(file_path+f"{file_type}", "w") as newfile:
        newfile.write("welcome to your newly created file!")
