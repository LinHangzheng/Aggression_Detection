#BSUB -q gpuq
#BSUB -o transfer.out
#BSUB -e transfer.err
#BSUB -n 1
#BSUB -R "select[ngpus>0] rusage[ngpus_shared=24]"
#BSUB -R span[ptile=2]
#BSUB -a python

CURDIR=$PWD
cd $CURDIR
python data_preprocess/opflow_to_npy.py

