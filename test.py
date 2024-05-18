import os

matching_files = []
directory=
C:\Users\uncun\Downloads\labo\SAT_instance\test
for filename in os.listdir(directory):
    print(f"{directory}/{filename}")
    with open(f"{directory}/{filename}")