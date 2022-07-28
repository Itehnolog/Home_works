import re
import os
import sys
import shutil
from pathlib import Path

"""
run: python clean.py "working_directory"
"""


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "i", "je", "ji", "g")
ARCHIVES = [".zip", ".gz", ".tar"]
VIDEO = [".avi", ".mp4", ".mov", ".mkv"]
AUDIO = [".mp3", ".ogg", "wav", "amr"]
DOCUMENTS = [".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx", ".xls"]
IMAGES = [".jpeg", ".png", ".jpg", ".svg"]


TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

# check and remove empty folder


def check_folder(path):
    for element in path.iterdir():
        if element.is_dir():
            if len(os.listdir(element)) == 0:
                os.rmdir(element)
            else:
                check_folder(element)

# move file depending on expension


def move_file(file: Path):
    ext = file.suffix
    if ext in VIDEO:
        new_path = work_folder / "video"
        new_path.mkdir(exist_ok=True, parents=True)
        shutil.move(file, new_path / normalize(file.name))
    elif ext in AUDIO:
        new_path = work_folder / "audio"
        new_path.mkdir(exist_ok=True, parents=True)
        shutil.move(file, new_path / normalize(file.name))
    elif ext in DOCUMENTS:
        new_path = work_folder / "documents"
        new_path.mkdir(exist_ok=True, parents=True)
        shutil.move(file, new_path / normalize(file.name))
    elif ext in IMAGES:
        new_path = work_folder / "images"
        new_path.mkdir(exist_ok=True, parents=True)
        shutil.move(file, new_path / normalize(file.name))
    elif ext in ARCHIVES:
        new_path = work_folder / "archives"
        new_path.mkdir(exist_ok=True, parents=True)
        folder_for_file = new_path / normalize(file.name, True)
        folder_for_file.mkdir(exist_ok=True, parents=True)
        shutil.unpack_archive(str(file.resolve()),
                              str(folder_for_file.resolve()))
        os.remove(file)
    else:
        new_path = work_folder / "orhers"
        new_path.mkdir(exist_ok=True, parents=True)
        shutil.move(file, new_path / normalize(file.name))

# normalize(tralation) name file


def normalize(name, folder=False):
    split_name = name.rsplit(".", 1)
    t_name = split_name[0].translate(TRANS)
    t_name = re.sub(r'\W', '_', t_name)
    if folder:
        return t_name
    else:
        new_name = t_name + "." + split_name[1]
        return new_name

# read folder for check if it's file


def read_folder(path) -> None:
    for element in path.iterdir():
        if element.is_dir():
            read_folder(element)
        else:
            move_file(element)


# check for correct input

if len(sys.argv) != 2:
    print("Incorrect input. Please input working folder")
    quit()


work_folder = Path(sys.argv[1])
read_folder(work_folder)
check_folder(work_folder)
