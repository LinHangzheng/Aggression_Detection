#BSUB -q gpuq
#BSUB -o movie_0.001_10.out
#BSUB -e movie_0.001_10.err
#BSUB -n 1
#BSUB -R "select[ngpus>0] rusage[ngpus_shared=24]"
#BSUB -R span[ptile=2]
#BSUB -a python
 
CURDIR=$PWD
cd $CURDIR
python VGG/VGG.py

