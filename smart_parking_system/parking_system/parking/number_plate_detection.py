import cv2
import pytesseract

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_number_plate(video_path):
    cap = cv2.VideoCapture(video_path)
    number_plate_text = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to grayscale and apply edge detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 170, 200)
        
        # Find contours in the edged image
        contours, _ = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        # Iterate over contours and look for rectangular contours
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 10, True)
            if len(approx) == 4:  # Detect rectangular shape for number plate
                x, y, w, h = cv2.boundingRect(approx)
                number_plate = frame[y:y+h, x:x+w]
                
                # Perform OCR to extract text
                text = pytesseract.image_to_string(number_plate, config='--psm 8')
                if text.strip():  # If text is found, return it
                    number_plate_text = text.strip()
                    print(f"Detected Number Plate: {number_plate_text}")
                    break

        if number_plate_text:
            break

    cap.release()
    cv2.destroyAllWindows()
    return number_plate_text if number_plate_text else "UNKNOWN"
