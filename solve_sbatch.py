import subprocess
import os
from concurrent.futures import ProcessPoolExecutor


def solve(file, root):
    filepath = os.path.join(root, file)
    print(filepath + ' is being solved...')
    # 要注意！SATソルバーの場所を移したらい動かないので変更すること。
    output_str = subprocess.run([r"/home/matsuse/test/kissat-master_3/build/kissat", "-s", "-n", filepath], capture_output=True, text=True).stdout
    output_dir = os.path.join(os.path.dirname(root), 'solved')
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = output_dir + '/' + file[:-3] + 'txt'
    with open(output_file_path, mode='w') as f:
        f.write(output_str)
    print('solved!')

def main():
    max_workers = os.cpu_count()

    #input_top_dir = input('Enter the directory where the .cnf is located:')
    input_top_dir = "/home/matsuse/SAT_instance/langford/test_for_sbatch"

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        for root, dirs, files in os.walk(top=input_top_dir):
            for file in files:
                if file.endswith('.cnf'):
                    executor.submit(solve, file, root)

if __name__ == "__main__":
    main()
