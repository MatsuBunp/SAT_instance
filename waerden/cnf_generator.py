import sys
import os

def make_cnf(j, k, n):
    # このファイルと同じ階層にcnfファイルを置くフォルダを作る
    script_saving_directory = f"{os.path.dirname(os.path.abspath(__file__))}/cnf"
    os.makedirs(script_saving_directory, exist_ok=True)

    filepath=f"{script_saving_directory}/waerden_{j}_{k}_{n}.cnf"

    with open(filepath, mode='w') as f:
        count = 0
        d=1
        while 1+2*d <= n :
            for i in range(1, n-(j-1)*d + 1):
                for val in range(j):
                    f.write(f'{i+val*d} ')
                f.write("0\n")
                count+=1
            d+=1

        d=1
        while 1+2*d <= n :
            for i in range(1, n-(k-1)*d + 1):
                for val in range(k):
                    f.write(f'{-(i+val*d)} ')
                f.write("0\n")
                count+=1
            d+=1
    with open(filepath, mode='r') as f:
        content = f.read()
    with open(filepath, mode='w') as f:
        f.seek(0, 0)  # ファイルの先頭に移動
        f.write(f'p cnf {n} {count}\n'+ content)
    return

j,k,n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]) 
make_cnf(j, k, n)
