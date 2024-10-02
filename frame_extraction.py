import cv2

def extract_frames(video_path, output_folder):
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(f"{output_folder}/frame{count}.jpg", image)  # Save frame as JPEG
        success, image = vidcap.read()
        count += 1
    return count
