import sys
import json

subjects = []

def convertData():
    #function to convert the JSON data into 2-D array
    input = sys.argv[1]
    data = json.loads(input)
    subject = []
    for key in data:
        for element in data[key]:
           subject.append(data[key][element])
        subjects.append(subject)
        subject = []
    return subjects

print(convertData())
