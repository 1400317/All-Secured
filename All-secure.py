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
    
    while(True):
    # Capture frame by frame
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
   
    #saving a test frame
    img = "test.png"
    cv2.imwrite(img, frame)
    
    #encode features of test pic.
    picture = face_recognition.load_image_file(img)
    encoding_picture1 = face_recognition.face_encodings(picture)

    if len(encoding_picture1) > 0:
         encoding_picture = face_recognition.face_encodings(picture)[0]    
    else:
        encoding_picture = encoding_person[0] + 1
    #solved the problem of non-existing of any face in the frame
    #close the door if no one is there
    print("testing")

   
    
