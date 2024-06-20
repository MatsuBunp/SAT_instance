#!/bin/bash
#SBATCH --partition=cpu0
#SBATCH --cpus-per-task=64
#SBATCH --mem-per-cpu=1000
#SBATCH --job-name=langford2
#SBATCH --output=lf.%J.out
#SBATCH --error=lf.%J.err
python /home/matsuse/SAT_instance/solve_sbatch2.py  ; curl -X POST -H "Authorization: Bearer WRJwYiiMQ7FoRBmiw1MnUcBedzTfuDq3Wmg6YSmKjdZ" -F "message=langford_21_100実行終了" https://notify-api.line.me/api/notify
RETCODE=$?
exit ${RETCODE}
