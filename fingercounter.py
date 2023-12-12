import cv2
import handtrackingmodule as htm

cap = cv2.VideoCapture(0)
pTime = 0
detector = htm.handDetector(detectionCon=0.75)
tipIds = [4, 8, 12, 16, 20]
largura_frame = int(cap.get(3))
altura_frame = int(cap.get(4))
tamanho = (largura_frame, altura_frame)
resultado = cv2.VideoWriter('filename.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, tamanho)

while True:
    sucesso, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        dedos = []

        # Polegar
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            dedos.append(1)
        else:
            dedos.append(0)

        # 4 Dedos
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                dedos.append(1)
            else:
                dedos.append(0)

        index_finger_pos = lmList[8]  
        print("posicao do indicador:", index_finger_pos)
    
        cv2.putText(img, str(dedos.count(1)), (35, 425), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 4)

    if sucesso == True:
        resultado.write(img)
        cv2.imshow('adedonhos godines', img)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
