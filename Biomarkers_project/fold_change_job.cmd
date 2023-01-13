#!/bin/bash
#SBATCH --job-name="fold_change_dicts"
#SBATCH --chdir=.
#SBATCH --output=fold_change_dicts.out
#SBATCH --error=fold_change_dicts.err
#SBATCH --ntasks=6
#SBATCH --cpus-per-task=24
#SBATCH --time=12:00:00
#SBATCH --qos=bsc_ls

module load python

/apps/GREASY/latest/INTEL/IMPI/bin/greasy LFC_tasks.dat
