import matplotlib.pyplot as plt


def psychometric_func(response, value):
    
    percent_corr=[]
    
    for i in range(0,len(response),4):
        percent_corr.append((response[i]+response[i+1]+response[i+2]+response[i+3])/4)
    plt.plot(value,percent_corr)
    plt.show()
