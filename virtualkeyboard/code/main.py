import cv2
import mediapipe as mp

webcam=cv2.VideoCapture(0)
webcam.set(3,1280)
webcam.set(4,960)

el=mp.solutions.hands
el_cizim=mp.solutions.drawing_utils

harfler = {
    "Q": [(40,40), (100,100)],
    "W": [(120,40), (180,100)],
    "E": [(200,40), (260,100)],
    "R": [(280,40), (340,100)],
    "T": [(360,40), (420,100)],
    "Y": [(440,40), (500,100)],
    "U": [(520,40), (580,100)],
    "I": [(600,40), (660,100)],
    "O": [(680,40), (740,100)],
    "P": [(760,40), (820,100)],
    "A": [(40,110), (100,170)],
    "S": [(120,110), (180,170)],
    "D": [(200,110), (260,170)],
    "F": [(280,110), (340,170)],
    "G": [(360,110), (420,170)],
    "H": [(440,110), (500,170)],
    "Z": [(40,180), (100,250)],
    "X": [(120,180), (180,250)],
}
basildi={}
yazi=""
with el.Hands(static_image_mode=False,max_num_hands=1,min_detection_confidence=0.5) as eller:
    while True:
        _,frame=webcam.read()
        frame=cv2.flip(frame,1)
        rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        result=eller.process(rgb)
        yukseklik,genislik,_=frame.shape

        if result.multi_hand_landmarks:
            for cizim in result.multi_hand_landmarks:
                koordinat1=cizim.landmark[8]
                koordinat2=cizim.landmark[12]
                x1 = int(koordinat1.x*genislik)
                y1 = int(koordinat1.y*yukseklik)
                x2 = int(koordinat2.x * genislik)
                y2 = int(koordinat2.y * yukseklik)
                cv2.circle(frame, (x1, y1), 4, (255, 0, 0), 12)
                cv2.circle(frame, (x2, y2), 4, (255, 0, 0), 12)

                for harf,koordinatlar in harfler.items():
                    x_min, y_min = koordinatlar[0]
                    x_max, y_max = koordinatlar[1]
                    if x_min<=x1<=x_max and y_min<=y1<=y_max and x_min<=x2<=x_max and y_min<=y2<=y_max:
                        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 0, 255), -1)
                        #cv2.rectangle(frame, (40, 300), (400, 360), (255, 255, 255), -1)
                        #cv2.putText(frame, harf, (60, 340), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
                        #cv2.putText(frame, yazi, (60, 340), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
                        if harf not in basildi or not basildi[harf]:
                            print(harf)
                            basildi[harf]=True
                            yazi=yazi+harf
                    else:
                        basildi[harf]=False

        for harf,koordinatlar in harfler.items():
            x_min, y_min = koordinatlar[0]
            x_max, y_max = koordinatlar[1]
            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 0, 255), 3)
            cv2.putText(frame, harf, (x_min+20, y_min+40), cv2.FONT_ITALIC, 1, (0, 0, 0), 2)

        cv2.rectangle(frame, (40, 300), (400, 360), (255, 255, 255), -1)
        cv2.putText(frame, yazi, (60, 340), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow("goruntu",frame)
        if cv2.waitKey(10) & 0xFF==ord("q"):
            break

webcam.release()
cv2.destroyAllWindows()











