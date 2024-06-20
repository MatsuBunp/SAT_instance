#!/bin/bash
#SBATCH --partition=cpu0
#SBATCH --cpus-per-task=32
#SBATCH --mem-per-cpu=200
#SBATCH --job-name=langford_sat
#SBATCH --output=sleep.%J.out
#SBATCH --error=sleep.%J.err
python /home/matsuse/SAT_instance/solve_sbatch.py