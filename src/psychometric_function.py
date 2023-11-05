import matplotlib.pyplot as plt


def psychometric_function(feedback,value,response):
    
    plt.plot(value,feedback, marker='o')
        # naming the x axis
    if response=='1' or response=='2':
        plt.xlabel('contrast')
    elif response=='3' or response=='4':
        plt.xlabel('spatial frequency')
    else:
        plt.xlabel('phase')

# naming the y axis
    plt.ylabel('percent correct')
    plt.title('Psychometric function')
   

    plt.show()
    plt.close()