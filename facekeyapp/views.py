from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
import base64
from django.views.decorators.csrf import csrf_exempt
import math
from deepface import DeepFace
from cvzone.FaceDetectionModule import FaceDetector
from PIL import Image
import io
from io import BytesIO
import threading 
import bbox


import json
import opencv
import cv2
import cvzone
import face_recognition
import numpy as np
from ultralytics import YOLO
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64

from django.http import JsonResponse
import base64

from PIL import Image
from io import BytesIO


from django.shortcuts import render








#################DB CONNECTION ND ENCODE FACES#########

import face_recognition
from PIL import Image
import io
import numpy as np
import mysql.connector




class main(View):
    list_people_encoding=[]

    def get(self,request):
  
        db_connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="1234",
            database="lk"
        )

        #list_people_encoding=[]
        #list_people_encoding1=self.list_people_encoding.copy()
        if db_connection.is_connected():
            print("connected")
            cursor = db_connection.cursor()


            query = f"SELECT img_data FROM images where username ='bibhu'"
            cursor.execute(query)

            results = cursor.fetchall()
            #print("output", results)
            for result in results:
                imd=result[0]
                #print("image" , imd)s
                #x=BytesIO(imd)
                #print(x.getvalue())  # Print the content of BytesIO
                img=Image.open(BytesIO(imd))
                # img.show()
                image_n = np.array(img)
                face_locations = face_recognition.face_locations(image_n)
                if face_locations:
                    face_encoding = face_recognition.face_encodings(image_n, known_face_locations=face_locations)[0]
                    #print(face_encoding)
                    self.list_people_encoding.append((face_encoding))
                #print(list_people_encoding)
            #print(list_people_encoding)
            
        cursor.close()
        db_connection.close()
        return render (request,'new.html')#{'posted':list_people_encoding1}


   

    ####################################################################################################################################


    def post(self,request):
        if request.method == 'POST':
            
            data = json.loads(request.body.decode('utf-8'))
            img_data = data.get('image')
            if img_data:
                
                _, imgstr = img_data.split(';base64,')
                img_bytes = base64.b64decode(imgstr)
                image = Image.open(BytesIO(img_bytes))
                #image.show()
                image_np = np.array(image)
                #print(image_np)
                #image_n = cv2.imread(image_np)
                image_array = np.frombuffer(img_bytes, dtype=np.uint8)
                imag = cv2.imdecode(image_array, cv2.IMREAD_COLOR)


        
        
                target_encoding = face_recognition.face_encodings(imag)
                #print(target_encoding)
                #confidence = 0.3
                model = YOLO("C:/Users/bibhu/OneDrive/Documents/GitHub/facelock/facekeyapp/models/best.pt")
                classNames = ["fake", "real"]
                results= model(imag,stream=True)
                
                

                for r in results:
                    #print("bibbbbbb")
                    boxes = r.boxes
                    for box in boxes:
                        #print("lala")
                        #print(box)
                        # BoundingBox
                        x1, y1, x2, y2 = box.xyxy[0]
                        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                        # cv2.rctangle(img,(x1,1),(2,y2),(255,0,255),3
                        w, h = x2 - x1, y2 - y1
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
                                # try:
                                
                                for person in self.list_people_encoding:
                                    encoded_face=person
                                    
                                    #print("hello")
                                    is_target_face=face_recognition.compare_faces(encoded_face,target_encoding)
                                    

                                    if face_location:
                                        face_number=0
                                        for location in face_location:
                                            if is_target_face[face_number]:
                                                print("AUTHORISED USER")
                                                return JsonResponse({'output':'authorizedUser'})
                                            else:
                                                face_number += 1
                                #  if not is_target_face[face_number]:
                                #             raise stopallloops
                                # except stopallloops:
                         
                                # print("UNAUTHORISED USER")
                                            
                                                
                                #                     if not is_target_face[face_number]:
                                #                         raise stopallloops
                                # except stopallloops:       
                                #     print("UNAUTHORISED USER")                                
                                    #response = HttpResponse("UNAUTHORISED user")
                    
        print("hhh")
        return JsonResponse({'output':'unauthorizedUser'})
          

































################################################################################################
                        
    # video_stream_app/views
    # def index(request
    #     return render(request, 'video_stream_app/index.html')

    # def upload_video(request):
    #     # Handle video upload and processing here
    #     # For simplicity, this example doesn't handle the actual video upload
    #     return JsonResponse({'status': 'success'})

                                  
                                            #return response2
            # Process the image or save it to the server
            # For instance, you can save it to a Django model's ImageField
            # example_model.image_field.save('filename.jpg', image_file, save=True)
            
            # Return a success response
        #     result = helper_function()  # Calling the helper function
        # return HttpResponse(res
        

#@csrf_exempt  # Use this decorator if you're handling POST requests without CSRF token (not recommended for production)



        
        # result = helper_function()  # Calling the helper function
        # return HttpResponse(result)
    #     return JsonResponse({'message': 'Image data received successfully'})
    # else:
    #     return JsonResponse({'message': 'Invalid request'}, status=400)

        

    
    # def handle_image(self,request):
        # uploaded_image = request.FILES['image']
        # new_image = Image(image_file=uploaded_image)
     #   new_image.save()
        # Perform additional tasks with the uploaded image if needed
        # return HttpResponse(# Render a success page or redirect as needed
        #return render(request, 'upload.html')  # Render the upload form
        
        
        
        # result = self.isreal()  # Calling second method
        # return HttpResponse(isreal)
        #isreal(image_data)
        # else:
        #     return  HttpResponse({'error': 'Invalid request method'}, status=405)
        




# def helper_function():
# #camera = cv2.VideoCapture(0)  # For Webcam
# # camera.set(3, 640)
# # camera.set(4, 480)
#     detector = FaceDetector()
#     confidence = 0.6
#     model = YOLO("C:/Users/bibhu/IdeaProjects/FACEUNLOCK/pyscript/bestfc prj.pt")
#     classNames = ["fake", "real"]
#     list_people_encoding=[]
#     s=image
#     s.show()

#     ##prev_frame_time = 0
#     ##new_frame_time = 0

#     frame_rate = 10
#     prev = 0

#     s = True

#     while s:
#         success,imgd = image.read()
#         time_elapsed = time.time() - prev
#         image, bboxs = detector.findFaces(imgd, draw=True)
#         if time_elapsed > 1./frame_rate:
#             prev = time.time()
#             target_encoding = face_recognition.face_encodings(imgd)
#             results = model(imgd, stream=True)
#             for r in results:
#                 boxes = r.boxes
#                 img,bboxs = detector.findFaces(imgd,False)
#                 for box in boxes:
#                     # Bounding Box
#                     x1, y1, x2, y2 = boxes.xyxy[0]
#                     x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
#                     cv2.rectangle(image,(x1,y1),(x2,y2),(0,0,0),1)
#                     # w, h = x2 - x1, y2 - y1
#                     # cvzone.cornerRect(image, (x1, y1, w, h))
#                     # Confidence
#                     conf = math.ceil((boxes.conf[0] * 100)) / 100
#                     # Class Namech
#                     cls = int(boxes.cls[0])
#                     if conf > confidence:
#                         if classNames[cls] == 'real':
#                                 #find_target_face()
#                                 face_location=face_recognition.face_locations(imgd)
#                                 for person in list_people_encoding:
#                                     encoded_face=person
#                                     #filename=person[1]
#                                     print("gudu")

#                                     is_target_face=face_recognition.compare_faces(encoded_face,target_encoding)
#                                     #print(f'{is_target_face} {filename}')

#                                     if face_location:
#                                         face_number=0
#                                         for location in face_location:
#                                             if is_target_face[face_number]:
#                                                 #label=filename
#                                                 return HttpResponse("Authorised User")
#                                             else:
#                                                 face_number += 1
#                                 else:
#                                     return HttpResponse("Unkown User")
#                         else:
#                             break
    # views.p


    










