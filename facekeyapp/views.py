from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
import base64
from django.views.decorators.csrf import csrf_exempt
import math

from PIL import Image
from io import BytesIO


import json
import cv2
import face_recognition
import numpy as np
from ultralytics import YOLO

import mysql.connector
import cvzone
from cvzone.FaceDetectionModule import FaceDetector
import bbox




class main(View):
    list_people_encoding=[]
    def get(self,request):
        #response = self.generating_face_encoding(username="nithi")
        return render (request,'tem.html')


    def post(self,request):
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            imgs = data.get('image')
            username='nithi'
            response = self.generating_face_encoding(username)   #username = data.get('username')
            # if(response == "Face recognition disabled"):
            #     return JsonResponse({'output':response})
            
          
            
            # for img_data in imgs:
            if imgs :     
                    _, imgstr = imgs.split(';base64,')
                    img_bytes = base64.b64decode(imgstr)
                    image = Image.open(BytesIO(img_bytes))
                    #image.show()
                    #image_np = np.array(image)
                    #print(image_np)
                    #image_n = cv2.imread(image_np)
                    image_array = np.frombuffer(img_bytes, dtype=np.uint8)
                    imag = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
                    detector=FaceDetector()
                    img,bboxs = detector.findFaces(imag, draw=True)

            
            
                    target_encoding = face_recognition.face_encodings(imag)
                    #print(target_encoding)
                    #confidence = 0.3
                    model = YOLO("C:\\Users\\bibhu\\OneDrive\\Documents\\GitHub\\testfacelock\\testfl\\testflapp\\models\\best.pt")
                    classNames = ["fake", "real"]
                    results= model(img,stream=True)
                    
                    

                    for r in results:
                        #print("bibbbbbb")
                        boxes = r.boxes
                        for box in boxes:
                            
                            x1, y1, x2, y2 = box.xyxy[0]
                            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                            # cv2.rctangle(img,(x1,1),(2,y2),(255,0,255),3
                            # w, h = x2 - x1, y2 - y1
                            # Confidence
                            conf = math.ceil((box.conf[0] * 100)) / 100
                            # ClassName
                            cls = int(box.cls[0])
                            if conf > 0.5:
                                print("clear")

                                if classNames[cls] == 'real':
                            
                                    print("real")
                                    face_location=face_recognition.face_locations(imag)
                                    # try
                                    
                                    # print( self.list_people_encoding)
                                    for person in self.list_people_encoding:
                                        encoded_face=person
                                        
                                        
                                        try :
                                            is_target_face=face_recognition.compare_faces(encoded_face,target_encoding)
                                        except ValueError :
                                            continue

                                        
                                        
                                        if face_location:
                                            face_number=0
                                            for location in face_location:
                                                if is_target_face[face_number]:
                                                    print("AUTHORISED USER")
                                                    return JsonResponse({'output':'AuthorizedUser'})
                                                else:
                                                    # face_number += 1
                                                    print("UNAUTHORISED USER")
                                                    return JsonResponse({'output':'unauthorizedUser'})
                                        # person+=1
                                    
                                    

                                # else:
                                #     return JsonResponse({'output':'fakeimage'})
                                    #  if not is_target_face[face_number]:
                                    #             raise stopallloops
                                    # except stopallloops:
                            
                                    # print("UNAUTHORISED USER")
                                                
                                                    
                                    #                     if not is_target_face[face_number]:
                                    #                         raise stopallloops
                                    # except stopallloops:       
                                    #     print("UNAUTHORISED USER")                                
                                        #response = HttpResponse("UNAUTHORISED user")
                    else:
                        print("Fetching Data,Please wait")
                        return JsonResponse({'output':'Fetching Data,Please wait'})
            


    def generating_face_encoding(self, username):
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="pcr"
        )

        
        if db_connection.is_connected():
            print("connected")
            cursor = db_connection.cursor()

            # if username is None:
            #     query = f"SELECT face_recognizing_data FROM pcr.t_users"  
            # else:
            #      query = f"SELECT face_recognizing_data FROM pcr.t_users where username='nithi'"

            query = f"SELECT face_recognizing_data FROM pcr.t_users where username='nithi' AND is_face_recognition_enabled = TRUE"

            cursor.execute(query)
            results = cursor.fetchall()

            if (len(results) > 0):
                for result in results:
                    imd=result[0]
                    img=Image.open(BytesIO(imd))
                    #img.show()
                    image_n = np.array(img)
                    face_locations = face_recognition.face_locations(image_n)
                    if face_locations:
                        face_encoding = face_recognition.face_encodings(image_n, known_face_locations=face_locations)[0]
                        self.list_people_encoding.append((face_encoding))
            else :
                return "Face recognition disabled"
            
        cursor.close()
        db_connection.close()
        return "Fetched successfully"































