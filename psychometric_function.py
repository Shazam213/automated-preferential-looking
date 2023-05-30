import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton

def psychometric_function(feedback,value,response):
    
    plt.plot(value,feedback)
        # naming the x axis
    if response=='1' or response=='2':
        plt.xlabel('contrast')
    else:
        plt.xlabel('spatial frequency')
# naming the y axis
    plt.ylabel('percent correct')
    plt.title('Psychometric function')
    def on_move(event):
        if event.inaxes:
            print(f'data coords {event.xdata} {event.ydata},',
                f'pixel coords {event.x} {event.y}')


    def on_click(event):
        if event.button is MouseButton.LEFT:
            print('disconnecting callback')
            plt.disconnect(binding_id)


    binding_id = plt.connect('motion_notify_event', on_move)
    plt.connect('button_press_event', on_click)

    plt.show()
    plt.close()