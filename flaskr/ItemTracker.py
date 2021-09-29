import cv2
import numpy as np
import time

class ItemTracker:

    def __init__(self, vidSource):
        self.vid = cv2.VideoCapture(vidSource)
        self.minContourSize = 950
        self.itemsFound = []
    
    def scan(self, numFrames=50):
        self.itemsFound = []
        for i in range(numFrames):
            ret, frame = self.vid.read()

            frame = cv2.blur(frame, (3,3))

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            ret, thresh = cv2.threshold(gray, 127, 255, 0)

            edges = cv2.Canny(gray, 50, 150)

            contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            #frame = cv2.GaussianBlur(frame, (k_size, k_size), gs_border)

            #frame = unsharp_mask(frame)

            filtCnt = []

            for cnt in contours:
                if cv2.contourArea(cnt) > self.minContourSize:
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

                location = self.getLocation(_cx, _cy, frame.shape[0], frame.shape[1])
                for i in range(x, x+w, 5) :
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
                if (code, location) not in self.itemsFound and len(code) == 3 : self.itemsFound.append((code, location))

        return self.itemsFound

    
    def getLocation(self, x, y, height, width):
        cx = width/2
        cy = height/2

        if x <= cx and y <= cy: return 1
        if x >= cx and y < cy: return 2
        if x <= cx and y >= cy: return 3
        if x >= cx and y >= cy: return 4

        return 0


            

            


# item = ItemTracker(1)

# print(item.scan(50))

