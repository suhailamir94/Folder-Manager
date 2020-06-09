import shutil
import os
import sys

from util import folder_to_file_mapping


class CleanFolder:

    """ Class to cleanup a folder.
        Takes in folder path as argument and move all files to relative folders acoording tom its extension.
    """

    def __init__(self, path):
        self.path = path
        self.all_files_and_folders = os.listdir(self.path)
        self.all_files_and_folders_updated = self.all_files_and_folders[:]

    def clean(self):
        for file in self.all_files_and_folders:
            self.move_file(file)

    def move_file(self, file):

        try:
            if "." in file and not os.path.isdir(os.path.join(self.path, file)):
                file_ext = file.split(".")[-1]
                folder_name = self.find_folder(file_ext)
                if folder_name:
                    if not folder_name[0] in self.all_files_and_folders_updated:
                        os.mkdir(os.path.join(self.path, folder_name[0]))
                        self.all_files_and_folders_updated.append(folder_name[0])
                    shutil.move(
                        os.path.join(self.path, file),
                        os.path.join(self.path, folder_name[0], file),
                    )
                else:
                    print(f"Sorry, we do not support .{file_ext} format yet.")

        except Exception as e:
            print(e)

    def find_folder(self, file_ext):
        return [
            folder
            for folder in folder_to_file_mapping.keys()
            if file_ext in folder_to_file_mapping[folder]
        ]


if __name__ == "__main__":
    if len(sys.argv) == 2:
        cf = CleanFolder(sys.argv[1])
        cf.clean()
    else:
        print("Please provide the folder path you want to clean")
