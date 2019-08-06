from datetime import datetime,date
from datetime import timedelta
from dateutil import parser
from dateutil.relativedelta import relativedelta
#from decimal import *
import sys, os
from math import pow, sqrt
import re
from hemingLib.readWrite import readFile, write_data_to_file
from hemingLib.headerReader import headersFound
from hemingLib.parseFile import getData
from hemingLib.DateDiff import getDateDiff
from hemingLib.parseDict import parseObservations, parsePredictions
from hemingLib.equationVars import get_slope_yIntercept
from hemingLib.compare import true_vs_measured_values
from hemingLib.errors import get_monthly_errors
from hemingLib.futures import predict_future

##NEED A BIG TRY EXCEPT FOR EACH PART
##INPUT AND STRING PROCESSING MODULE FUNCTION


##def readFile(inFile):
###checking if input file exists
##    try:
##        if not os.path.isfile(inFile):
##            raise FileNotFoundError
##        with open(inFile) as f:
##            #read File as one string
##             inString=f.read()
##
##        return inString
##    
##    except FileNotFoundError:
##        print("File {} doesn't exist. Exiting ...".format(inFile))
##        sys.exit() 



##def headersFound(fileString):
##    observPos=fileString.find('observaciones')
##    predictPos=fileString.find('predicciones')
##
##    missing=''
##    try:
##        if observPos==-1:
##            missing='observPos'
##            print("Input File missing observation data. Exiting ...")
##            sys.exit()
##        elif predictPos==-1:
##            missing='predictPos'
##
##        if (len(missing)>0):
##            raise ValueError
##
##        return(observPos,predictPos)
##
##    except ValueError:
##            print("Input File missing {} data. Exiting ...".format(missing))
##            sys.exit()
##            

##def getData(observations_Pos, predictions_Pos,inFstring):
##    if observations_Pos>predictions_Pos:
##            splitter=inFstring.split("observaciones")
##            observBlock=splitter[1]
##            predictBlock=splitter[0].split("predicciones")[1]
##    else:
##            splitter=inFstring.split("predicciones")
##            predictBlock=splitter[1]
##            observBlock=splitter[0].split("observaciones")[1]
##
##    observSplit=observBlock.split("\n")
##    if len(observSplit)>1:
##        observLines=observSplit[1:]
##        temp=[]
##        for x in observLines:
##            flag=False
##            #remove 
##            if bool(re.match("\s+$",x)) or bool(re.match("\t+$",x)) or x=="":
##                flag=True
##                    
##            if not flag:
##                temp.append(x)
##        observLines=temp
##     #   print((observLines))
##   
##    predictSplit=predictBlock.split("\n")
##    temp=[]
##    if len(predictSplit)>1:
##        predictLines=predictSplit[1:]
##        for x in predictLines:
##            flag=False
##            if bool(re.match("\s+$",x)) or bool(re.match("\t+$",x)) or x=="":
##                flag=True
##                    
##            if flag==False:
##                temp.append(x)
##        predictLines=temp
##    #    print((predictLines))
##
##    empty=""
##    try:
##        if len(observLines)==0:
##            empty="observation data"
##            
##        elif len(predictLines)==0:
##            empty="prediction data"
##
##        if (len(empty)>0):
##            raise Exception
##
##        return(observLines,predictLines)
##    except Exception:
##        print("Missing {} in file. Insert a new file with both observation and prediction data".format(empty))
##        sys.exit()
##        

##def getDateDiff(observation_lines):
##    daysList=[]
##    try:
##        for line in observation_lines:
##            observLineSplit=line.split(' ')
##            observLineSplit = ' '.join(observLineSplit).split()
##            day=observLineSplit[0]
##            time=observLineSplit[1]
##            dateDetails=day+' '+time
##            a=parser.parse(dateDetails)
##            datetime_obj = parser.parse(dateDetails).date()
##            if datetime_obj not in daysList:
##                daysList.append(datetime_obj)
##
##        print(len(daysList))
##    except ValueError:
##        print("date missing in string or incorrect syntax ...Exitting")
##        sys.exit()
##
##    try:
##    #    print(daysList)
##        print('min date: {}, max date: {}'.format(min(daysList),max(daysList)))
##        abc=daysList[-1]-daysList[0]
##        flag=False
##        if abc.days <= 365:
##            flag=True
##        else:
##            raise Exception
##        return flag
##    except Exception:
##        print('date range exceeds over one year. Enter file with max one year range. Exitting...')
##        sys.exit()

##def parseObservations(observLines):
##    observationsDay={}
##    for line in observLines:
##        observLineSplit=line.split(' ')
##        observLineSplit = ' '.join(observLineSplit).split()
##        day=observLineSplit[0]
##        time=observLineSplit[1]
##        dateDetails=day+' '+time
##        dateHour=parser.parse(dateDetails)
##        productionObserv=observLineSplit[2]
##        windSpeed=observLineSplit[3]
##        data={}
##        data['speed']=windSpeed
##        data['production']=productionObserv
##        observationsDay[dateHour]=data
##    return observationsDay

##def parsePredictions(predictionLines):
##    predictionsDay={}
##    for line in predictionLines:
##        predictLineSplit=line.split(' ')
##        predictLineSplit = ' '.join(predictLineSplit).split()
##        day=predictLineSplit[0]
##        time=predictLineSplit[1]
##        dateDetails=day+' '+time
##        dateHour=parser.parse(dateDetails)
##        speedPredict=predictLineSplit[2]
##        data={}
##        data['speed']=speedPredict
##        predictionsDay[dateHour]=data
##    return predictionsDay

##def get_slope_yIntercept(observations):
##    n=len(observations)
##    sigma_x=0
##    sigma_y=0
##    observationKeys=list(observations.keys())
##
##    for key in observationKeys:
##        sigma_x=sigma_x+int(observations[key]['speed'])
##        sigma_y=sigma_y+int(observations[key]['production'])
##
##    #using equations from https://en.wikipedia.org/wiki/Deming_regression
##    y_bar=sigma_y/n
##    x_bar=sigma_x/n
##
##    sigma_xi_sub_x_bar=[]
##    sigma_yi_sub_y_bar=[]
##
##    for key in observationKeys:
##        x=int(observations[key]['speed'])
##        x_xBar= x - x_bar
##        y=int(observations[key]['production'])
##        y_yBar= y - y_bar
##        sigma_xi_sub_x_bar.append(x_xBar)
##        sigma_yi_sub_y_bar.append(y_yBar)
##
##    x_pow2=0
##    y_pow2=0
##    x_y_mul=0
##
##    for i in range(len(sigma_xi_sub_x_bar)):    
##        x_diff = sigma_xi_sub_x_bar[i]
##        x_pow2= x_pow2 + pow(x_diff,2)
##        y_diff = sigma_yi_sub_y_bar[i]
##        y_pow2 = y_pow2 + pow(y_diff,2)
##        x_y_mul = x_y_mul + (x_diff*y_diff)
##
##    s_xx = x_pow2 / (n-1)
##    s_yy = y_pow2 / (n-1)
##    s_xy = x_y_mul / (n-1)
##
##    syy_xx = s_yy - s_xx
##    mul_S_xy = 4 * pow(s_xy , 2)
##    sqrt_beta_1 = sqrt( pow(syy_xx,2) + mul_S_xy)
##
##    beta_1= (syy_xx + sqrt_beta_1) / (2*s_xy)
##    beta_0= y_bar - (beta_1 * x_bar)
##
##    print('slope: {}, y-intercept: {}'.format(beta_1, beta_0))
##    return beta_1,beta_0

#compares values obtained from measurement to those that lie on the curve 
##def true_vs_measured_values(observationsDict, slope, y_intercept):
##    observationKeys=list(observationsDict.keys())
##    reading=[]
##    months=[]
##    mon_Num=0
##    monthlyDict={}
##    key=observationKeys[0]
##    start_month=key
##    end_month=start_month+relativedelta(months=1)
##
##    for i in range(len(observationKeys)):
##        key=observationKeys[i]
##        
##        if key<=end_month:
##            speed = int(observationsDict[key]['speed'])
##            info={}
##            info['speed']=speed
##            info['observation']= int(observationsDict[key]['production'])
##            info['prediction']= y_intercept + (slope*speed)
##            monthlyDict[key]=info
##            if i==len(observationKeys)-1:
##                months.append(monthlyDict)
##        else:
##            months.append(monthlyDict)
##            monthlyDict={}
##            key=observationKeys[i]
##            start_month=key
##            end_month=start_month+relativedelta(months=1)
##          
##    return months
                
##def get_monthly_errors(MONTHS):
##    MAE_Values={}
##    MSE_Values={}
##
##    diff_Obs_Prd={}
##    sum_Obs={}
##    diff_Obs_Prd={}
##    n={}
##    for i in range(len(MONTHS)):
##        tot_Obsv=0
##        absValue=0
##        sqValue=0
##        monthly_n=0
##        for j in MONTHS[i]:
##            obsrv=MONTHS[i][j]['observation']
##            predict=MONTHS[i][j]['prediction']
##            absValue+= abs( obsrv - predict )
##            sqValue+= pow ( absValue,2 )
##            tot_Obsv+=obsrv
##            monthly_n+=1
##
##        MAE=100*absValue/tot_Obsv
##        root=sqrt (sqValue/monthly_n)
##        MSE=100*monthly_n*root/tot_Obsv
##
##        MAE_Values[i+1]=MAE
##        MSE_Values[i+1]=MSE
##        
####        diff_Obs_Prd[i+1]=absValue
####        sum_Obs[i+1]=tot_Obsv
####        diff_Obs_Prd[i+1]=sqValue
####        n[i+1]=monthly_n
####
####        print("value is {}".format())
####
##    ##for k in range(len(sum_Obs)):
####        MAE=100*(diff_Obs_Prd[i+1]/sum_Obs[i+1])
##        
####        MSE=100*(n[i+1]) * (sqrt (diff_Obs_Prd[i+1]/n[i+1]) )/ sum_Obs[i+1]
##        
##        
##    return MAE_Values, MSE_Values


##def predict_future(predictionDict,slope,y_Intercept):
##    future_expect={}
##    data={}
##    for i in predictionDict:
##        speed=int(predictionDict[i]['speed'])
##        predictedProd=slope*speed+y_Intercept
##        print((i))
##        data['speed']=speed
##        data['production']=predictedProd
##        future_expect[i]=data
##        data={}
##
##    return future_expect



##def write_data_to_file(slope,y_intercept, MAE_dict, MSE_dict,future_dict,outFile):
##
##    slope_delimited=float("{0:.2f}".format(slope))
##    y_intercept_delimited=float("{0:.2f}".format(y_intercept))
##    measurement_keys=list(MAE_dict.keys())
##    print(measurement_keys)
##    keyList=list(future_dict.keys())
##    
##    with open(outFile,'a') as f:
##        f.write('{} {}\n'.format(slope_delimited,y_intercept_delimited))
##        for key in measurement_keys:
##            MAE=float("{0:.2f}".format(MAE_dict[key]))
##            MSE=float("{0:.2f}".format(MSE_dict[key]))
##            f.write('Month{} {} {}\n'.format(key,MAE,MSE))
##        for k in keyList:
##            date=str(k)
##            date=str(date)[:-3]
##            prod=int(future_dict[k]['production'])
##            f.write('{} {}\n'.format(date,prod))  
    
     

def main():
    inputFile=sys.argv[1]
    outputFile=sys.argv[2]
    oneString=readFile(inputFile)
    observationLoc, predictionLoc=headersFound(oneString)
    observationLines,predictionLines=getData(observationLoc,predictionLoc,oneString)
    flag=getDateDiff(observationLines)
    observationDetails={}
    if flag:
        observationDetails=parseObservations(observationLines)
    beta1,beta0=get_slope_yIntercept(observationDetails)
    monthsSplit=true_vs_measured_values(observationDetails,beta1,beta0)
    MAE_value, MSE_value=get_monthly_errors(monthsSplit)
    predictionDetails=parsePredictions(predictionLines)
    futureDict=predict_future(predictionDetails,beta1,beta0)
    write_data_to_file(beta1,beta0,MAE_value,MSE_value,futureDict,outputFile)

    
    
    
    
if __name__== "__main__":
      main()

        
