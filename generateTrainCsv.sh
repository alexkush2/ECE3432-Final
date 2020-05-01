#!/bin/bash

if command -v svn >/dev/null 2>&1 ; then
    echo "Running generateTrainCsv.sh"
else
    echo "Error! svn not found!"
    echo "try 'sudo apt install subversion' and re-run this script."
fi

# number of images to add to training file
num=5000

# if argument is given then use that as the number of images to use
if [ $# = 1 ]
then 
    num=$1
fi
echo "Using $num training images"

# see if data/images exists
if [ ! -d data/images/ ]
then
    # if not download images
    mkdir data/images
    cd data
    echo 'downloading images'
    svn checkout https://github.com/lbaitemple/race-car/trunk/data/images > /dev/null 2>&1
    cd ..
fi


# see if data/list exists
if [ -d data/list/ ]
then
    # if it does then does the csv file exist?
    if [ -e data/list/train_1.csv ]
    then
        # if yes, remove csv
        echo "Removing pre-existing train_1.csv"
        rm data/list/train_1.csv
    fi
# if not make directory
else
    echo "Making /data/list dir"
    mkdir data/list
fi

# add the word 'image' to top of file
echo "Creating train_1.csv"
echo image >> data/list/train_1.csv

# add $num number of random images to the file
find data -name '*.jpg' | shuf -n $num >> data/list/train_1.csv