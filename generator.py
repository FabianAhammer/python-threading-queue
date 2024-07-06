# Generator will ignore already published files and overwrite with new data
import os
import shutil

import numpy as np

categories = 6
subFiles = 6


def create_file_name(category: int, file_entry: int):
    if category < 0 or category > 26:
        raise Exception("Invalid category, only max alphabet allowed!")
    return "data/"+str(chr((ord('A') + category))) + str(file_entry) + ".txt"


if "data" in os.listdir():
    shutil.rmtree("data")
    # os.rmdir("data")
    print("Removed old dir!")

os.mkdir("data")
for cat in range(categories):
    for sub in range(subFiles):
        file_name = create_file_name(cat, sub)
        array = np.zeros((1, 14, 256, 320))
        np.random.shuffle(array)
        array.tofile(file_name, "", "%s")
print("Done")
