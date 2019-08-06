#returns observation data split into 30 days periods
from dateutil.relativedelta import relativedelta

def true_vs_measured_values(observationsDict, slope, y_intercept):
    observationKeys=sorted(list(observationsDict.keys()))
    reading=[]
    months=[]
    mon_Num=0
    monthlyDict={}
    key=observationKeys[0]
    start_month=key
    end_month=start_month+relativedelta(months=1)
    for i in range(len(observationKeys)):
        key=observationKeys[i]
        if key<=end_month:

            speed = int(observationsDict[key]['speed'])
            info={}
            info['speed']=speed
            info['observation']= int(observationsDict[key]['production'])
            info['prediction']= y_intercept + (slope*speed)
            monthlyDict[key]=info
            if i==len(observationKeys)-1:
                months.append(monthlyDict)
        else:
            months.append(monthlyDict)
            monthlyDict={}
            key=observationKeys[i]
            start_month=key
            end_month=start_month+relativedelta(months=1)
    return months
