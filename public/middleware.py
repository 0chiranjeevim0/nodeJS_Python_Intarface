import sys
import json
from main import invoke
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


def parseData(index):

    #converting data for a particlar array into object
    staff_order = {}
    res = invoke()
    data = res[index]
    pointer = 1

    period = []

    for i in data:
        name = 'order_'+str(pointer)
        for j in i:
          period.append(j)
        staff_order[name] = period
        period = []
        pointer +=1


    return staff_order
    
def appendMaster():
    time_table = {}
    for i in range(0,5):
        name = 'year_'+str(i+1)
        res = parseData(i+1)
        time_table[name] = res

    return time_table



val = appendMaster()
print(json.dumps(val))
