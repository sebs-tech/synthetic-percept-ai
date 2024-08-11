import tensorflow as tf

import numpy as np
import cv2
import matplotlib.pyplot as plt

# Mediapipe 
import mediapipe as mp

mp_holistic = mp.solutions.holistic
mp_drawing  = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

def available_gpu():
    print(tf.config.list_physical_devices('GPU'))
    
    
    
if __name__ == '__main__': 
    #available_gpu()
    
    img = cv2.imread('/home/user/dev/AI/synthetic-percept-ai/data/dataset/shark/shark0.png', 0) 
   # plt.imshow(img, cmap='gray')
   
   # Show the image
    #cv2.imshow('image',img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()