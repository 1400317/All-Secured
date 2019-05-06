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


                            #training
while (i<x):
    #get the training img location from the user
    photo = input ("the location of pic of person%d: " %i)
    face = photo.replace('\\' , '/')
    #solved the problem of recieving the escape char '\' in the location input by the user
    
    #reading my pic.& adding it to a list
    person = face_recognition.load_image_file(face)
    persons.append (person)
    
    #encoding face features from my pic. & adding it to a list
    encoding_person = face_recognition.face_encodings(person)[0]
    encoding_persons.append (encoding_person)
   
    i = i+1
   
    
