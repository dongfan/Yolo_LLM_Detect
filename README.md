# ✋ YOLO + LLM Rock-Paper-Scissors Detector

웹캠 화면에서 손을 실시간으로 인식하고,  
LLM을 활용해 **가위 / 바위 / 보** 제스처를 판별하는 프로젝트입니다.

YOLO는 빠른 손 검출을 담당하고,  
LLM은 이미지 기반 의미 추론을 담당합니다.

---

## ✅ 주요 기능

- USB 웹캠 실시간 스트리밍
- YOLO 모델로 Hand Bounding Box 감지
- Crop된 손 이미지를 LLM에 전달
- 가위 / 바위 / 보 결과 출력 및 오버레이 표시
- `q` 키로 종료
- 확장 가능 (게임 로직, TensorRT, Web UI 등)

---

## 📂 프로젝트 구조

