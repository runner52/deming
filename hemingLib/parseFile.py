import re

def getData(observations_Pos, predictions_Pos,inFstring):
    if observations_Pos>predictions_Pos:
            splitter=inFstring.split("observaciones")
            observBlock=splitter[1]
            predictBlock=splitter[0].split("predicciones")[1]
    else:
            splitter=inFstring.split("predicciones")
            predictBlock=splitter[1]
            observBlock=splitter[0].split("observaciones")[1]

    observSplit=observBlock.split("\n")
    if len(observSplit)>1:
        observLines=observSplit[1:]
        temp=[]
        for x in observLines:
            flag=False
            #remove 
            if bool(re.match("\s+$",x)) or bool(re.match("\t+$",x)) or x=="":
                flag=True
                    
            if not flag:
                temp.append(x)
        observLines=temp
     #   print((observLines))
   
    predictSplit=predictBlock.split("\n")
    temp=[]
    if len(predictSplit)>1:
        predictLines=predictSplit[1:]
        for x in predictLines:
            flag=False
            if bool(re.match("\s+$",x)) or bool(re.match("\t+$",x)) or x=="":
                flag=True
                    
            if flag==False:
                temp.append(x)
        predictLines=temp
    #    print((predictLines))

    empty=""
    try:
        if len(observLines)==0:
            empty="observation data"
            
        elif len(predictLines)==0:
            empty="prediction data"

        if (len(empty)>0):
            raise Exception

        return(observLines,predictLines)
    except Exception:
        print("Missing {} in file. Insert a new file with both observation and prediction data".format(empty))
        sys.exit()
        
