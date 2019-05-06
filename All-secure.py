# -*- coding: utf-8 -*-


import cv2
import face_recognition
import serial

#establish connection with arduino on port 
c = input ("Enter the COM port nubmer: ")
com= "COM{}".format (c)
arduino = serial.Serial(com, 9600)
print("Connection to arduino...")


                            #user inputs
y = input ("Enter number of persons allowed to enter the room: ")
x = int (y)
persons =[]
encoding_persons= []
i=0
