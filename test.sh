#!/bin/bash

my_function() {
    local my_array=("${!1}")
    echo "$(expr ${my_array[2]} + 3)"
}
my_array=(1 2 3 4 5)
my_function "my_array[@]"
