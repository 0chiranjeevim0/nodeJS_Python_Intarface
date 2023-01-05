import sys
import json
from main import invoke

year1 = []
year2 = []
year3 = []
year4 = []
year5 = []



def convertData(currentYear):
    sysin = sys.argv[1]
    subjects = json.loads(sysin)
    for i in subjects:
        lab = i["ISLab"]
        duration = str(i["duration"])
        staff = i["staff"]
        subject = i["subject"]
        subjectCode = i["subjectCode"]
        year = str(i["year"])

        if(currentYear == 1 and year == '1'):
            if(lab == "false"):
                year1.append(subjectCode+":"+subject+":"+staff+":"+duration)
            else:
                year1.append("lab"+":"+subjectCode+":"+subject+":"+staff+":"+duration)
        if(currentYear == 2 and year == '2'):
            if(lab == "false"):
                year2.append(subjectCode+":"+subject+":"+staff+":"+duration)
            else:
                year2.append("lab"+":"+subjectCode+":"+subject+":"+staff+":"+duration) 
        if(currentYear == 3 and year == '3'):
            if(lab == "false"):
                year3.append(subjectCode+":"+subject+":"+staff+":"+duration)
            else:
                year3.append("lab"+":"+subjectCode+":"+subject+":"+staff+":"+duration) 
        if(currentYear == 4 and year == '4'):
            if(lab == "false"):
                year4.append(subjectCode+":"+subject+":"+staff+":"+duration)
            else:
                year4.append("lab"+":"+subjectCode+":"+subject+":"+staff+":"+duration)
        if(currentYear == 5 and year == '5'):
            if(lab == "false"):
                year5.append(subjectCode+":"+subject+":"+staff+":"+duration)
            else:
                year5.append("lab"+":"+subjectCode+":"+subject+":"+staff+":"+duration)       
               

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


def convertDatas():
    for i in range(1,5):
        convertData(i)

    subjectDict = {

        1:year1,
        2:year2,
        3:year3,
        4:year4,
        5:year5,
    }
    return subjectDict
res = convertDatas()
print(json.dumps(res))Z

#val = appendMaster()
#print(json.dumps(val))
