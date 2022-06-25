import cv2
import mediapipe as mp
import time
class handdetector():
    def __init__( self , static_image_mode=False,max_num_hands=2 , model_complexity=1,min_detection_confidence=0.5,min_tracking_confidence=0.5):
        #static_image_mode=False,
               #max_num_hands=2,
               #model_complexity=1,
               #min_detection_confidence=0.5,
               #min_tracking_confidence=0.5):
        self.static_image_mode = static_image_mode
        self.max_num_hands = max_num_hands
        self.model_complexity = model_complexity
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence
        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands(self.static_image_mode,self.max_num_hands,self.model_complexity,self.min_detection_confidence,self.min_tracking_confidence)
        self.mpdraw = mp.solutions.drawing_utils
    def findhands(self,img,draw=True):
        imgrgb = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgrgb)
        #print(result.multi_hand_landmarks)
        if self.result.multi_hand_landmarks:
            for handlms in self.result.multi_hand_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(img , handlms , self.mphands.HAND_CONNECTIONS)
        return img
    def findposition(self,img,handnum=0,draw = True):
        lmlist = []
        if self.result.multi_hand_landmarks:
            myhand = self.result.multi_hand_landmarks[handnum]
            for id , lm in enumerate(myhand.landmark):
                #print(id,lm)
                h , w ,c = img.shape
                cx , cy = int(lm.x*w) , int(lm.y*h)
                lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),10,(255,0,255),cv2.FILLED)
        return lmlist
def main():
    video = cv2.VideoCapture(0)
    detctor = handdetector()
    ptime =0
    ctime = 0
    while True:
            check, img = video.read()
            #img = cv2.resize(image , (960,980))
            img = detctor.findhands(img)
            lmlist = detctor.findposition(img)
            ctime = time.time()
            if len(lmlist) !=0:

                print(lmlist[4])
            fps = 1/(ctime - ptime)
            ptime = ctime
            cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,255),3)
            cv2.imshow('Color Frame', img)
            key = cv2.waitKey(50)
            if key == ord('q'):
                    break
if __name__ == "__main__":
    main()
