import cv2
from yolo_detector import HandDetector
from llm_classifier import LLMClassifier

detector = HandDetector()
classifier = LLMClassifier()

cap = cv2.VideoCapture(0)  # USB 웹캠 연결

if not cap.isOpened():
    print("❌ 웹캠을 열 수 없습니다.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ 프레임을 읽을 수 없습니다.")
        break

    hands = detector.detect(frame)

    for (x1, y1, x2, y2) in hands:
        crop = frame[y1:y2, x1:x2]

        rps = classifier.classify(crop)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(frame, rps, (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        print("🖐 LLM 판단:", rps)

    cv2.imshow("YOLO + LLM RPS Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
