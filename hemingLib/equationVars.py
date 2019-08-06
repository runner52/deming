#calculates values of beta 0 and beta 1

from math import pow, sqrt

def get_slope_yIntercept(observations):
    n=len(observations)
    sigma_x=0
    sigma_y=0
    observationKeys=list(observations.keys())

    for key in observationKeys:
        sigma_x=sigma_x+int(observations[key]['speed'])
        sigma_y=sigma_y+int(observations[key]['production'])

    #using equations from https://en.wikipedia.org/wiki/Deming_regression
    y_bar=sigma_y/n
    x_bar=sigma_x/n

    sigma_xi_sub_x_bar=[]
    sigma_yi_sub_y_bar=[]

    for key in observationKeys:
        x=int(observations[key]['speed'])
        x_xBar= x - x_bar
        y=int(observations[key]['production'])
        y_yBar= y - y_bar
        sigma_xi_sub_x_bar.append(x_xBar)
        sigma_yi_sub_y_bar.append(y_yBar)

    x_pow2=0
    y_pow2=0
    x_y_mul=0

    for i in range(len(sigma_xi_sub_x_bar)):    
        x_diff = sigma_xi_sub_x_bar[i]
        x_pow2= x_pow2 + pow(x_diff,2)
        y_diff = sigma_yi_sub_y_bar[i]
        y_pow2 = y_pow2 + pow(y_diff,2)
        x_y_mul = x_y_mul + (x_diff*y_diff)

    s_xx = x_pow2 / (n-1)
    s_yy = y_pow2 / (n-1)
    s_xy = x_y_mul / (n-1)

    syy_xx = s_yy - s_xx
    mul_S_xy = 4 * pow(s_xy , 2)
    sqrt_beta_1 = sqrt( pow(syy_xx,2) + mul_S_xy)

    beta_1= (syy_xx + sqrt_beta_1) / (2*s_xy)
    beta_0= y_bar - (beta_1 * x_bar)

    print('slope: {}, y-intercept: {}'.format(beta_1, beta_0))
    return beta_1,beta_0
