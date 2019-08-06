

def predict_future(predictionDict,slope,y_Intercept):
    future_expect={}
    data={}
    for i in predictionDict:
        speed=int(predictionDict[i]['speed'])
        predictedProd=slope*speed+y_Intercept
        print((i))
        data['speed']=speed
        data['production']=predictedProd
        future_expect[i]=data
        data={}

    return future_expect
