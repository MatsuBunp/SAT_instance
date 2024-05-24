#!/bin/bash

cnf_make(){
    local index=0
    local array=("${!1}")    
    #echo "Array length: ${#array[@]}"
    for value in "${array[@]}"
    do
        if [ "$index" -ge 3 ]; then
            for n_range in {0..3}
            do
                #echo "Value: ${array[index]}, Index: $index, N_range: $n_range"
                python3 naive_waerden_cnf_maker.py "$2" "$index" "$(expr ${array[index]} + $n_range - 2)"
            done
        fi
        index=$((index+1))
    done
}

cnf_make "Wlist3[@]" 3
cnf_make "Wlist4[@]" 4
cnf_make "Wlist5[@]" 5
cnf_make "Wlist6[@]" 6
