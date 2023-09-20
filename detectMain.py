import torch
import cv2
import time

import serial  # tai pyserial - arduino-pyhon - arduinoserial

arduinoData = serial.Serial('com4', 9600) #serial
class_name = ['CAN', 'BOTTLE']  #dat ten cho 2 class
ID = ['0', '1'] #dat ID
my_model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5-master/best.pt') #same teacher, load model
cap = cv2.VideoCapture(1) #bat camera

while (True):
    ret, image_goc = cap.read()
    image_goc = cv2.resize(image_goc, (300, 250), fx=0.5, fy=0.5) #lam khung camera
    detections = my_model(image_goc)
    results = detections.pandas().xyxy[0].to_dict(orient="records") #chua hieu
    for result in results:
        class_name = result['name']
        ID = result['class']
        if ID == 0:
            x1 = int(result['xmin'])
            y1 = int(result['ymin'])
            x2 = int(result['xmax'])
            y2 = int(result['ymax'])
            cv2.rectangle(image_goc, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(image_goc, class_name, (x1 + 3, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (60, 255, 255), 1)
            print("CAN") #dong khung
            arduinoData.write('1'.encode())
        if ID == 1:
            u1 = int(result['xmin'])
            v1 = int(result['ymin'])
            u2 = int(result['xmax'])
            v2 = int(result['ymax'])
            cv2.rectangle(image_goc, (u1, v1), (u2, v2), (0, 0, 255), 2)
            cv2.putText(image_goc, class_name, (u1 + 3, v1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 1)
            print("BOTTLE")
            arduinoData.write('2'.encode())

    cv2.imshow("Oject_Dt", image_goc)
    if cv2.waitKey(25) & 0xFF == ord('a'):
        break

cap.release()
cv2.destroyAllWindows()