import subprocess
import pathlib
import os
from concurrent.futures import ProcessPoolExecutor

def solve(file, root):
    filepath = os.path.join(root, file)
    print(filepath + ' is being solved...')
    output_str = subprocess.run([r"/mnt/c/Users/uncun/Downloads/labo/hoge/build/kissat", "-s", "-n", "--time=5000", filepath], capture_output=True, text=True).stdout
    output_path = root + '5000s'
    os.makedirs(output_path, exist_ok=True)
    output_file_path = output_path + '/' + file[:-3] + 'txt'
    with open(output_file_path, mode='w') as f:
        f.write(output_str)
    print('solved!')

def main():
    max_workers = os.cpu_count()

    input_top_dir = f"{os.path.dirname(os.path.abspath(__file__))}/waerden_cnf"

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        for root, dirs, files in os.walk(top=input_top_dir):
            for file in files:
                if file.endswith('1133.cnf'):
                    executor.submit(solve, file, root)

if __name__ == "__main__":
    main()
