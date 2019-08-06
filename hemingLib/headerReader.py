#checks for observaciones and predicciones keywords and data
import sys

def headersFound(fileString):
    observPos=fileString.find('observaciones')
    predictPos=fileString.find('predicciones')

    missing=''
    try:
        if observPos==-1:
            missing='observPos'
            print("Input File missing observation data. Exiting ...")
            sys.exit()
        elif predictPos==-1:
            missing='predictPos'

        if (len(missing)>0):
            raise ValueError

        return(observPos,predictPos)

    except ValueError:
            print("Input File missing {} data. Exiting ...".format(missing))
            sys.exit()
            


