import os
from pathlib import Path

file_path = "./txt"
output_path = "merged_label.txt"

path_list = os.listdir(file_path)

with open(output_path, "w") as output:
    for path in path_list:
        data_path = Path(os.path.join("filelsit/Data0924/image", path.replace("txt", "bmp"))).as_posix()
        output.write(data_path + " ")
        with open(os.path.join(file_path, path), 'r') as f:
            for line in f.readlines():
                line = line.rstrip("\n")
                output.write(line + " ")
            output.write("\n")


 