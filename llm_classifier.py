from openai import OpenAI
from PIL import Image
import io

client = OpenAI()

class LLMClassifier:
    def classify(self, crop_frame):
        # 이미지 crop → PNG byte 변환
        img = Image.fromarray(crop_frame)
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        img_bytes = buf.getvalue()

        prompt = "이 손 모양은 가위, 바위, 보 중 무엇인가요? 한 단어로만 답해주세요."

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {"role": "user", "content": prompt},
                {"role": "user", "image": img_bytes},
            ]
        )

        return response.output_text.strip()
