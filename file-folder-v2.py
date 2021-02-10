import os


class FolderFileCreator:
    def making_directory(self):
        parent_dir = r"F:\OneDrive\Skrivebord"
        directory = input(
            "what do you want your directory to be called: ").strip().title()
        global dir_path
        dir_path = os.path.join(parent_dir, directory)
        os.mkdir(dir_path)

    def making_file(self):
        file_type = input(
            "what file type do you want your file to be: ").lower()
        file = input(
            "what do you want your file to be called: ").strip().title()
        file_path = os.path.join(dir_path, file)
        with open(file_path+f"{file_type}", "w") as newfile:
            newfile.write("welcome to your newly created file!")
