import cv2
import os
import PIL
import pathlib
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow_datasets as tfds
from skimage import io
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import speech_recognition as sr
import pyttsx3
import pyaudio


#photo reader
# def image():
#     img_path = "bass.jpg"
#     image = cv2.imread(img_path)
#     cv2.imshow('the image', image)
#     # print("Shape: {}".format(image.shape))
#     cv2.waitKey(0)
#     print(cv2.imwrite('bass/modified.png',image))



#viddeo Reader
# video=cv2.VideoCapture(0)
# while True:
#     grabbed , frame = video.read()
#     frame = cv2.resize(frame,(800,500))
#
#     if cv2.waitKey(0) & 0xFF:
#         break
#     cv2.imshow('video',video)
#
# video.release()
# cv2.destroyAllWindows()

#converting speech to text
r=sr.Recognizer()
while True:

    with sr.Microphone() as source:
        try:
            print("speak anyting")
            r.adjust_for_ambient_noise(source, duration=.01)
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()
            print(text)

        except:
            print("couldn't understand audio")
