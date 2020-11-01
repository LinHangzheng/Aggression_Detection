#BSUB -q gpuq
#BSUB -o VGG/all_100_5.out
#BSUB -e VGG/all_100_5.err
#BSUB -n 1
#BSUB -R "select[ngpus>0] rusage[ngpus_shared=24]"
#BSUB -R span[ptile=2]
#BSUB -a python

CURDIR=$PWD
cd $CURDIR
python VGG/VGG.py

