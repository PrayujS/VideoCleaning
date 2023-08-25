import cv2

input_file = 'TrimmedVideo.mp4'
output_file = 'FinalVideo.mp4'

# Open the input video
cap = cv2.VideoCapture(input_file)

# Get the video's frames per second (fps) and frame size
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the cropping region
x = 196
y = 0
width = 959
height = 694

# Define the codec and create the VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Crop the frame
    cropped_frame = frame[y:y+height, x:x+width]

    # Write the cropped frame to the output video
    out.write(cropped_frame)

    cv2.imshow('Cropped Video', cropped_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()