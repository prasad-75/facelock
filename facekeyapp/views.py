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



class main(View):
    list_people_encoding=[]


    def post(self,request):
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            imgs = data.get('image')
            response = self.generating_face_encoding( username = data.get('username'))
            if(response == "Face recognition disabled"):
                return JsonResponse({'output':response})
            
            for img_data in imgs:
               if img_data :     
                    _, imgstr = img_data.split(';base64,')
                    img_bytes = base64.b64decode(imgstr)
                    image = Image.open(BytesIO(img_bytes))
                    # image.show()
                    #image_np = np.array(image)
                    #print(image_np)
                    #image_n = cv2.imread(image_np)
                    image_array = np.frombuffer(img_bytes, dtype=np.uint8)
                    imag = cv2.imdecode(image_array, cv2.IMREAD_COLOR)


            
            
                    target_encoding = face_recognition.face_encodings(imag)
                    #print(target_encoding)
                    #confidence = 0.3
                    model = YOLO("C:\\Users\\srina\\OneDrive\\Documents\\GitHub\\facelock\\facekeyapp\\models\\best.pt")
                    classNames = ["fake", "real"]
                    results= model(imag,stream=True)
                    
                    

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
                                print("bibhu")

                                if classNames[cls] == 'real':
                            
                                    print("prasad")
                                    # class stopallloops(Exception):
                                    #      pass 
                                    face_location=face_recognition.face_locations(imag)
                                    # try
                                    # print("encodings")
                                    # print( self.list_people_encoding)
                                    for person in self.list_people_encoding:
                                        encoded_face=person
                                        
                                        #print("hello")
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
                                                    face_number += 1
                                        person+=1
                                    return JsonResponse({'output':'unauthorizedUser'})
                                else:
                                    return JsonResponse({'output':'fakeimage'})
                                    #  if not is_target_face[face_number]:
                                    #             raise stopallloops
                                    # except stopallloops:
                            
                                    # print("UNAUTHORISED USER")
                                                
                                                    
                                    #                     if not is_target_face[face_number]:
                                    #                         raise stopallloops
                                    # except stopallloops:       
                                    #     print("UNAUTHORISED USER")                                
                                        #response = HttpResponse("UNAUTHORISED user")
                    
        print("unauthorizedUser")
        return JsonResponse({'output':'no user detected'})
          


    def generating_face_encoding(self, username):
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1210",
            database="pcr"
        )

        
        if db_connection.is_connected():
            print("connected")
            cursor = db_connection.cursor()


            query = f"SELECT face_recognizing_data FROM t_users WHERE username = '"+username+"' AND is_face_recognition_enabled = TRUE"
            cursor.execute(query)

            results = cursor.fetchall()
            if (len(results) > 0):
                for result in results:
                    imd=result[0]
                    #x=BytesIO(imd)
                    #print(x.getvalue())  # Print the content of BytesIO
                    img=Image.open(BytesIO(imd))
                    # img.show()
                    image_n = np.array(img)
                    # print(image_n)
                    face_locations = face_recognition.face_locations(image_n)
                    if face_locations:
                        face_encoding = face_recognition.face_encodings(image_n, known_face_locations=face_locations)[0]
                        #print(self.face_encoding)
                        self.list_people_encoding.append((face_encoding))
                        #self.face_encoding
                    # print("db")
                    # print(self.list_people_encoding)
                #print(list_people_encoding)
            else :
                return "Face recognition disabled"
            
        cursor.close()
        db_connection.close()
        return "Fetched successfully"































