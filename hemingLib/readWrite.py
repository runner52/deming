import os, sys

def readFile(inFile):
#checking if input file exists
    try:
        if not os.path.isfile(inFile):
            raise FileNotFoundError
        with open(inFile) as f:
            #read File as one string
             inString=f.read()

        return inString
    
    except FileNotFoundError:
        print("File {} doesn't exist. Exiting ...".format(inFile))
        sys.exit() 

def write_data_to_file(slope,y_intercept, MAE_dict, MSE_dict,future_dict,outFile):

    slope_delimited=float("{0:.2f}".format(slope))
    y_intercept_delimited=float("{0:.2f}".format(y_intercept))
    measurement_keys=list(MAE_dict.keys())
    print(measurement_keys)
    keyList=list(future_dict.keys())
    
    with open(outFile,'a') as f:
        f.write('{} {}\n'.format(slope_delimited,y_intercept_delimited))
        for key in measurement_keys:
            MAE=float("{0:.2f}".format(MAE_dict[key]))
            MSE=float("{0:.2f}".format(MSE_dict[key]))
            f.write('Month{} {} {}\n'.format(key,MAE,MSE))
        for k in keyList:
            date=str(k)
            date=str(date)[:-3]
            prod=int(future_dict[k]['production'])
            f.write('{} {}\n'.format(date,prod))  
