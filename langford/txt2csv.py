import os
import pandas as pd
import re

def main():
    records = []
    input_dir = f"{os.path.dirname(os.path.abspath(__file__))}/solved_5000s"

    files = sorted(os.listdir(input_dir), key=lambda x: tuple(map(int, re.findall(r'\d+', x))))

    for file in files:
        if file.endswith('.txt'):
            filepath=os.path.join(input_dir, file)
            with open(filepath, 'r') as f:
                content = f.read()
                # 名前
                shorten_filename = file[9:][:-4]
                # 変数、節の数
                var_cls = re.search(r'p cnf (\d+) (\d+)', content)
                var_num = int(var_cls.group(1))
                cls_num = int(var_cls.group(2))
                # 求解時間
                last_seconds_index = content.rfind("seconds")
                content_before_last_seconds = content[last_seconds_index-30:last_seconds_index+10] 
                seconds_match = re.search(r'(\d+\.\d+|\d+)\s+seconds', content_before_last_seconds)
                seconds = seconds_match.group(1) if seconds_match else None
                # SATかUNSATか。時間切れの問題は本来はSATかUNSATかを調べる
                tresult=''
                if 'UNSATISFIABLE' in content:
                    result = 'u'
                elif 'SATISFIABLE' in content:
                    result = 's'
                else:
                    result = 'x'
                    if int(shorten_filename)%4==0 or int(shorten_filename)%4==3:
                        tresult = 's'
                    else: 
                        tresult = 'u'
                
                records.append({
                    'Problem': shorten_filename, 
                    'Var_num': var_num,
                    'Cls_num': cls_num,
                    'Result': result, 
                    'TResult':tresult, 
                    'Time': seconds})
            

    df = pd.DataFrame(records)
    output_csv_path = f"{os.path.dirname(os.path.abspath(__file__))}/results.csv"
    df.to_csv(output_csv_path, index=False)


if __name__ == "__main__":
    main()
