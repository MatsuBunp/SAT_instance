# SAT_instance
まとめて処理する場合はsolve2txt.pyを使うが，ソルバーの参照場所はあらかじめ設定しないと動かないので注意．
# ファイルの使い方
SATソルバーの応用問題の実践．練習を兼ねる．
１．waerden数
naive_waerden_cnf_maker.py<br>
コマンド：-.py j k n<br>
j,k,nは正の整数　．暗黙にj,k<nを仮定する．<br>
出力：　「j個の等間隔に並ぶ0も，k個の等間隔に並ぶ1も含まないような長さnの二進列x_1,...,x_n」が存在するか，すなわちそのような二進数の割当x_1,...,x_nが存在するための条件（CNF式）<br>
このファイルと同じディレクトリにwaerden_j_k_n.cnfが作成される．<br>
備考：TAOCP 4巻の最初の「単純な例」に沿って作っている．　なお，n<W(j,k)←→SATである．<br>
・まとめてcnf式を生成するにはcnf_generator_main.shなど．
