#BSUB -q gpuq
#BSUB -o npyI.out
#BSUB -e npyI.err
#BSUB -n 1
#BSUB -R "select[ngpus>0] rusage[ngpus_shared=24]"
#BSUB -R span[ptile=2]
#BSUB -a python

CURDIR=$PWD
cd $CURDIR
python npy2image.py

