#generates values of Mean Absoluate Error and Mean Square Error
from math import sqrt

def get_monthly_errors(MONTHS):
    MAE_Values={}
    MSE_Values={}

    diff_Obs_Prd={}
    sum_Obs={}
    diff_Obs_Prd={}
    n={}
    for i in range(len(MONTHS)):
        tot_Obsv=0
        absValue=0
        sqValue=0
        monthly_n=0
        for j in MONTHS[i]:
            obsrv=MONTHS[i][j]['observation']
            predict=MONTHS[i][j]['prediction']
            absValue+= abs( obsrv - predict )
            sqValue+= pow ( absValue, 2 )
 #           if monthly_n== len(MONTHS[i-1]):
     #           print(sqValue)
            tot_Obsv+=obsrv
            monthly_n+=1

        MAE=100*absValue/tot_Obsv
        root=sqrt (sqValue/monthly_n)
        MSE=100*monthly_n*root/tot_Obsv

        MAE_Values[i+1]=MAE
        MSE_Values[i+1]=MSE
           
    return MAE_Values, MSE_Values
