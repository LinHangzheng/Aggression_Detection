#BSUB -q gpuq
#BSUB -o VGG/Test_all_youtube_10.out
#BSUB -e VGG/Test_all_youtube_10.err
#BSUB -n 1
#BSUB -R "select[ngpus>0] rusage[ngpus_shared=24]"
#BSUB -R span[ptile=2]
#BSUB -a python

CURDIR=$PWD
cd $CURDIR
python VGG/test.py

