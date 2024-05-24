import sys
import os



def make_cnf(n):
    # このファイルと同じ階層にcnfファイルを置くフォルダを作る
    script_saving_directory = f"{os.path.dirname(os.path.abspath(__file__))}/cnf"
    os.makedirs(script_saving_directory, exist_ok=True)

    filepath=f"{script_saving_directory}/langford_{n}.cnf"

    # 本体
    # 排他的な節を返す
    def S(a):
        result=[]
        result.append(' '.join(map(str, a))+' 0')
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                result.append(f'-{a[i]} -{a[j]} 0')
        return result

    length = n
    sum = 0
    list=[]
    x_index=[]

    for i in range(1, length+1):
        list.append([k for k in range(sum+1, sum+2*length-i)]) # d_1~n
        x_index.append(sum)
        sum += 2*length-i-1
    def x2y(a, b):
        return x_index[a-1]+b
    list.append([i+1 for i in x_index]) # s_1
    list.append([i+2 for i in x_index]) # s_2
    for i in range(3, 2*length+1):
        tekitou=[x2y(j, i-j-1) for j in range(1, i-1) if j <= length] + [x2y(j, i) for j in range(1, 2*length-i) if j<=length]
        #tekitou=[x2y(j, i) for j in range(1, 2*length-i) if i<2*length-1]
        list.append(tekitou)

    with open(filepath, 'w') as f:
        for i in range(len(list)):
            for item in S(list[i]):
                f.write(item+'\n')
    # 節数などの情報を記載し、重複行を削除する
    with open(filepath, 'r', encoding='utf-8') as f:
        unique_lines = set(f.readlines())
        line_count = len(unique_lines)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f'p cnf {int(1.5*length*(length-1))} {line_count}\n')
        f.writelines(unique_lines)
    return

beginning, end = int(sys.argv[1]), int(sys.argv[2])
#beginning, end = 5,5
for n in range(beginning, end+1):
    make_cnf(n)



