import cv2
import numpy as np

def getTextOverlay(input_image):
    l_black = np.array([0,0,0])
    u_black = np.array([15,15,15])
    overlay = cv2.inRange(input_image,l_black,u_black)
    output = cv2.bitwise_not(overlay)
    return output

if __name__ == '__main__':
    image = cv2.imread('simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imwrite('simpons_text.png', output)