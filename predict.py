#from datetime import datetime,date
#from datetime import timedelta
#from dateutil import parser
#from dateutil.relativedelta import relativedelta
#from decimal import *
import sys#, os
#from math import pow, sqrt
#import re
from hemingLib.readWrite import readFile, write_data_to_file
from hemingLib.headerReader import headersFound
from hemingLib.parseFile import getData
from hemingLib.DateDiff import getDateDiff
from hemingLib.parseDict import parseObservations, parsePredictions
from hemingLib.equationVars import get_slope_yIntercept
from hemingLib.compare import true_vs_measured_values
from hemingLib.errors import get_monthly_errors
from hemingLib.futures import predict_future    
     

def main():
    inputFile=sys.argv[1]
    outputFile=sys.argv[2]
    print("reading input file...")
    oneString=readFile(inputFile)
    print("checking input file headers...")
    observationLoc, predictionLoc=headersFound(oneString)
    print("parsing observations and predictions...")
    observationLines,predictionLines=getData(observationLoc,predictionLoc,oneString)
    print("checking dates...")
    flag=getDateDiff(observationLines)
    observationDetails={}
    if flag:
        print("fetching observations data...")
        observationDetails=parseObservations(observationLines)
        print("fetching predictions data")
        predictionDetails=parsePredictions(predictionLines)
    print("getting beta1 and beta0 values....")
    beta1,beta0=get_slope_yIntercept(observationDetails)
    print("splitting data into months....")
    monthsSplit=true_vs_measured_values(observationDetails,beta1,beta0)
    print("getting MAE and MSE values for each month...")
    MAE_value, MSE_value=get_monthly_errors(monthsSplit)
    print("predicting the future, generating predicted values...")
    futureDict=predict_future(predictionDetails,beta1,beta0)
    print("writing data to {} ...".format(outputFile))
    write_data_to_file(beta1,beta0,MAE_value,MSE_value,futureDict,outputFile)
    print("Congrats! execution has finished")
    
if __name__== "__main__":
      main()

        
