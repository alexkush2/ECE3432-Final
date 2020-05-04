#!/usr/bin/env python3

import json
import pandas as pd
import time

from av_nn_tools import NNTools
from av_parse_data import ParseData

TEST_LIST = "data/list/test_1.csv"
SETTINGS = "data/set_accuracy_test.json"

try:
    data = pd.read_csv(TEST_LIST)
except:
    print("Error! you are missing test_1.csv")
    exit()

parsedata = ParseData()
with open(SETTINGS) as fp:
    content = json.load(fp)

    shape = content['shape']
    servo_pred = NNTools(content["servo_setting"])
    servo_pred.load_model(content['servo_model'])

servo_count = 0

total_time = 0

for index in range(len(data)):
    _, servo, motor = parsedata.parse_data(data["image"][index])

    start_time = time.time()
    pred_servo = servo_pred.predict(data["image"][index])
    end_time = time.time()
    total_time += (end_time - start_time)

    if abs(servo - pred_servo) <= content['error_margin']:
        # print(servo)
        servo_count += 1
    # if (servo-15)*(pred_servo-15) >= 0:
    #     # print(servo)
    #     servo_count += 1


    if (index + 1) % 100 == 0:
        print("[%5d] servo: %2.2f " % \
              (index + 1, 100 * servo_count / (index + 1), ))


servo_pred.test(TEST_LIST)

# print("servo: %2.2f" % (100 * servo_count / (index + 1)))

total_time = total_time / len(data)

print("Servo Accuracy: %2.2f" % (100 * servo_count / (index + 1)))
print("Average Time: " + str(total_time))