import matplotlib.pyplot as plt
import numpy as np
import cv2

def vis(item, sort_name, pivot=None):
    fig, ax = plt.subplots()
    if pivot:
        ax.bar(x= range(len(item)), height=item)[pivot].set_color('r')
        plt.title('Sorting....')
    else:
        ax.bar(x= range(len(item)), height=item)
        plt.title('Sorted')
    fig.canvas.draw()
    plt.close()
    X = np.array(fig.canvas.renderer.buffer_rgba())
    cv2.imshow(sort_name, X)
    ms= 1 if pivot is not None else 0
    if cv2.waitKey(ms) & 0xFF==ord('q'):
        cv2.destroyAllWindows()
        raise SystemExit
