import cv2

cap = cv2.VideoCapture(0)
while True:
    # # Read a frame and return a boolean; 'true' if read, else 'fasle'; 2nd return is on frame captured
    ret, frame = cap.read()

    if not ret:
        break

    # show that one frame which is returned above from webcam & keep looping inside while loop
    cv2.imshow('Webcam Feed -  Press "q" to quit', frame)

    # Exit on pressing 'q'
    # For the lowercase letter q, the ASCII code is 113 in decimal and 71 in hexadecimal.
    # Condider below condition with Operator precedence as :: ( cv2.waitKey(1) & 0xFF) == (ord('q'):)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
