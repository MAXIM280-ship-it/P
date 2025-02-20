import cv2

# Replace with your IP camera's stream URL
url = 0  # Example URL format

cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Display the frame
        cv2.imshow('IP Camera Feed', frame)

        # Exit on ESC
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()