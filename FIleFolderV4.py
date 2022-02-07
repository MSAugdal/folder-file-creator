import os
from time import sleep


def folderFileCreator():
    parent_dir = r"path to where you want the file to be created. example: C:\desktop"
    file_types = [".py", ".txt", ".csv"]

    while True:
        directory = input(
            "what do you want your directory to be called: ").strip().title()
        dir_path = os.path.join(parent_dir, directory)
        try:
            os.mkdir(dir_path)
        except Exception as ex:
            print(ex)
            print("\nthis directory already exists.")
            print("please choose a new name.\n")
        else:
            print("\nyour directory was successfully created.")
            break

    while True:
        print(f"\nchoose any of the following file types")
        print(file_types)
        file_type = input(
            "which file type do you want your file to be: ").replace(" ", "").strip().lower()

        if file_type not in file_types:
            print("\nplease enter a valid file type.")
        else:
            file = input(
                "\nwhat do you want your file to be named: ").replace(" ", "").strip().title()
            file_path = os.path.join(dir_path, file)

            with open(file_path+file_type, "w") as newfile:
                if file_type == ".py":
                    newfile.write(
                        "# welcome to your newly created python file!")
                elif file_type == ".txt":
                    newfile.write("welcome to your newly created text file!")
                elif file_type == ".csv":
                    newfile.write("welcome to your newly created csv file!")

            print("\nyour file was successfully created.\n")
            print("process finished.")
            print("you can now enjoy your new directory and file!")
            sleep(3)
            break


if __name__ == "__main__":
    folderFileCreator()
