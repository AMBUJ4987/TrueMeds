from paddleocr import PaddleOCR
import numpy as np

ocr = PaddleOCR(
    use_angle_cls=True,
    lang="en",
    show_log=False
)
def extract_text(image_path):

    result = ocr.ocr(image_path, cls=True)

    text = []
    confidence = []

    if result and result[0]:

        for line in result[0]:

            text.append(line[1][0])
            confidence.append(line[1][1])

    return {
        "ocr_text": " ".join(text),
        "confidence": np.mean(confidence) if confidence else 0
    }


# ----------------------------
# Test the module
# ----------------------------
if __name__ == "__main__":

    result = extract_text(
        r"E:\TrueMeds\DATASET\demo_metronidazole.jpg"
    )

    print(result)