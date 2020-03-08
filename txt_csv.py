import pandas as pd
import os
import csv
dire = "/home/shsheikh/Music/RADOMEH"
for file in os.listdir(dire):
    print(file)
    full_path = os.path.join(dire, file)
    with open(full_path, 'r') as inp:
        
        #with open(file.split(".")[0], 'w') as output:
        strip = (line.strip() for line in inp)
        lines = (line.split(",") for line in strip if line)

        with open(full_path.split(".")[0] + ".csv", 'w+') as out:
            writer = csv.writer(out)
            writer.writerows(lines)
#    df = pd.read_fwf(file)
#    new_file_name = file.split(".")[0]
#    df.to_csv(file)
       # print(file)
