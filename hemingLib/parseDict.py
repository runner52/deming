#parsing input file to get data of  in each of the sections of observations and predictions
from dateutil import parser

def parseObservations(observLines):
    observationsDay={}
    for line in observLines:
        observLineSplit=line.split(' ')
        observLineSplit = ' '.join(observLineSplit).split()
        day=observLineSplit[0]
        time=observLineSplit[1]
        dateDetails=day+' '+time
        dateHour=parser.parse(dateDetails)
        productionObserv=observLineSplit[2]
        windSpeed=observLineSplit[3]
        data={}
        data['speed']=windSpeed
        data['production']=productionObserv
        observationsDay[dateHour]=data
    return observationsDay

def parsePredictions(predictionLines):
    predictionsDay={}
    for line in predictionLines:
        predictLineSplit=line.split(' ')
        predictLineSplit = ' '.join(predictLineSplit).split()
        day=predictLineSplit[0]
        time=predictLineSplit[1]
        dateDetails=day+' '+time
        dateHour=parser.parse(dateDetails)
        speedPredict=predictLineSplit[2]
        data={}
        data['speed']=speedPredict
        predictionsDay[dateHour]=data
    return predictionsDay
