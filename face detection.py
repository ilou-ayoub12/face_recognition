# FACE DETECTOR APP
import cv2
train_face_data=cv2.CascadeClassifier('open.xml')
#img=cv2.imread('pf.jfif')#to realqqqqqqqqqqqQqd the img
#img=cv2.imread('wac.jpeg')#to read the img
#-*************************vedio detection***************************************
webcam=cv2.VideoCapture(0)# 0 which mean the camera of a loptop if we want to upload a vedio from laptop cv2.VideoCapture(''name.mp4) and the programe stills the same
# DETECT FACES IN A VEDEO: FOr that we goin to use an other variakle Webcam and than we use a loop to read wht exist in the farme of the rectangle
### iterate forever over frame
while True:
###Read the curent frame
 succeful_frame_read, frame=webcam.read() # as u see theis loop returns two things first thing are succeful_frame_read it s always true,and frame it s the image:
 # so for that we have to chanfe the img existed in the program of detection img by frame
 gray_vedeo=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
 face_coord=train_face_data.detectMultiScale(gray_vedeo)
 for (x,y,w,h) in face_coord:
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
 cv2.imshow('the hero ',frame)
 key=cv2.waitKey(1) #like this it gonna wait for a click to take an other pic but if we put 1 like this Cv2.waitKey(1) gonna wait one ms take a pic and of course it won t quit cuz we have a loop 
# BUT naow we can ot quit the loop so when tha cam work we wont able to quit 
# for that we will use a specific ke to quit
 if key==81 or key==113:#this number from ASCII code 81=Q 113=q
    break
## and also we need to release the the vedeoCaptur
webcam.release()
#***********************************end of webcam/vedeo detector*********************************

#------------------That its for the image---------------------
"""#cv2.waitKey()# able us to see the pic cuz we syop the prom for tha 
# AS we said we make it black and white: for that we use the function CvtColor "convert coler"
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#WE WILL DISPLAY IT 
cv2.imshow('the hero ',gray_img)
#cv2.waitKey()
# now we will detect faces
# for that we use detecMultiScale this function going to give us the coordns of the face
face_coord=train_face_data.detectMultiScale(gray_img)
#print(face_coord)# dispalyin the coordn
# now we have the coord let draw the rectangle ,(0,255,0) to choose the green color,2 it s for the thickess of the recatangle
#(x,y,w,h)=face_coord[0]# this can detect one face so if we have more face we will use the loop
for (x,y,w,h) in face_coord:
  cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
cv2.imshow('the hero ',img)
cv2.waitKey()"""
#------------------------the end of image detectio---------------------
