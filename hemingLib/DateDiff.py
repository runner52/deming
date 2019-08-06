#checks if dates exist in input file and if the max range is 1 year
from dateutil import parser
import sys, os

def getDateDiff(observation_lines):
    daysList=[]
    try:
        for line in observation_lines:
            observLineSplit=line.split(' ')
            observLineSplit = ' '.join(observLineSplit).split()
            day=observLineSplit[0]
            time=observLineSplit[1]
            dateDetails=day+' '+time
            a=parser.parse(dateDetails)
            datetime_obj = parser.parse(dateDetails).date()
            if datetime_obj not in daysList:
                daysList.append(datetime_obj)
    except ValueError:
        print("date missing in string or incorrect syntax ...Exitting")
        sys.exit()

    try:
        print('min date: {}, max date: {}'.format(min(daysList),max(daysList)))
        abc=daysList[-1]-daysList[0]
        flag=False
        if abc.days <= 365:
            flag=True
        else:
            raise Exception
        return flag
    except Exception:
        print('date range exceeds over one year. Enter file with max one year range. Exitting...')
        sys.exit()
