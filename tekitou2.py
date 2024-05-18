import subprocess
import pathlib
import os
from concurrent.futures import ProcessPoolExecutor

def main():

    input = f"{os.path.dirname(os.path.abspath(__file__))}/waerden_cnf"
    filepath = input + "/waerden_6_6_1133.cnf"
    output_str = subprocess.run([r"/mnt/c/Users/uncun/Downloads/labo/hoge/build/kissat", "-s", "-n", filepath], capture_output=True, text=True).stdout
    output_path = input + '/test2.txt'
    with open(output_path, mode='w') as f:
        f.write(output_str)
    print('solved!')

if __name__ == "__main__":
    main()
