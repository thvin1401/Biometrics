import cv2
import os

INPUT_DIR = "input"
OUTPUT_DIR = "output"

def equalize_color_image(image):
    # Convert to YCrCb color space
    ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

    # Split channels
    y, cr, cb = cv2.split(ycrcb)

    # Equalize histogram on Y channel (luminance)
    y_eq = cv2.equalizeHist(y)

    # Merge channels
    ycrcb_eq = cv2.merge((y_eq, cr, cb))

    # Convert back to BGR
    result = cv2.cvtColor(ycrcb_eq, cv2.COLOR_YCrCb2BGR)

    return result


def process_images():

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for file in os.listdir(INPUT_DIR):

        input_path = os.path.join(INPUT_DIR, file)

        if not file.lower().endswith((".png", ".jpg", ".jpeg")):
            continue

        img = cv2.imread(input_path)

        if img is None:
            print(f"Skipping {file}")
            continue

        result = equalize_color_image(img)

        output_path = os.path.join(OUTPUT_DIR, file)

        cv2.imwrite(output_path, result)

        print(f"Processed: {file}")


if __name__ == "__main__":
    process_images()