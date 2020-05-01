# ECE3432-Final
https://github.com/alexkush2/ECE3432-Final

## Inital Setup on Pi
Run setup script to install libraries and download all images
`./setup.sh`

## Run Testing
Run model testing script to test image prediction 
`python3 rcCarModelTest.py`
Prints out total accumulated loss, accuracy, predicted value and the time it took to predict on one image

### My testing resutls from pi
![Test Results](snip.PNG)

## Configuration
### JSON files contained in /data
JSON files used for setting up training, testing, and accuracy test parameters

### Generate New Testing Data
Run the following script with an argument of how many images you want in your testing dataset
`generateTrainCsv.sh <NumImages>`
