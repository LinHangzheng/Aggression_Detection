#BSUB -q nodeq
#BSUB -o SC.out
#BSUB -e SC.err
#BSUB -n 10
#BSUB -R span[ptile=2]
#BSUB -a python
 
CURDIR=$PWD
cd $CURDIR
python videos_to_images\&opflow.py

