import cv2
import time
import numpy as np
import pyzbar.pyzbar as pyzbar


vid = cv2.VideoCapture(1)
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

olret, oldFrame = vid.read()
text = 'none'

k_size = 0
gs_border = 3



while True:
    ret, frame = vid.read()

    #frame = cv2.flip(frame, 1)
    
    frame = cv2.blur(frame, (3,3))
    #frame = cv2.resize(frame,(420, 420) )

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    ret, thresh = cv2.threshold(gray, 127, 255, 0)

    edges = cv2.Canny(gray, 50, 150)

    contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #frame = cv2.GaussianBlur(frame, (k_size, k_size), gs_border)

    #frame = unsharp_mask(frame)

    filtCnt = []

    for cnt in contours:
        if cv2.contourArea(cnt) > 950:
            filtCnt.append(cnt)

    cv2.drawContours(frame, filtCnt, -1, (255,255,0), 1)


    for cnt in filtCnt:
        x,y,w,h = cv2.boundingRect(cnt)
        croppedFrame = frame[y + 10:y+h - 10, x + 10:x+w - 10]
        croppedFrame = cv2.Canny(croppedFrame, 50, 150)
        croppedHsv = hsv[y:y+h, x:x+w]
        ctr, heir = cv2.findContours(croppedFrame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        code = ''
        _cx, _cy = int(x+w/2), int(y+h/2)
        for i in range(x, x+w, 10) :
            #if cv2.contourArea(c) < 50: continue
            #_x,_y,_w,_h = cv2.boundingRect(c)
            #print(_cx)
            #print(_cy)
            color = hsv[_cy, i, 0]
            #print(color)

            #if(color < 5 or color > 160): None
            if (color < 10 or color > 155):
                if '1' not in code: code = code + '1'
            elif (50 < color < 85):
                if '2' not in code: code = code + '2'
            elif (28 < color < 35):
                #if 'Y' not in code: code = code + 'Y'
                None
            elif (100 < color < 130 ):
                if '3' not in code: code = code + '3'
            else:
                None
        cv2.drawContours(frame, filtCnt, -1, (255,255,0), 1)
        cv2.putText(frame, code, (int(x+w/2), int(y+h/2)), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
        print(code)


    cv2.imshow("frame", frame)

    

    #if (frame.alql != oldFrame.all):
    #text = pytesseract.image_to_string(frame, lang='eng')

    #decodedObjs = pyzbar.decode(frame)



    #print(decodedObjs)

    oldFrame = frame

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

    #time.sleep(2)
