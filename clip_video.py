import cv2
import sys
import os

if __name__ =='__main__':
    # check if video arg is correct
    # input_path ouput_path start stop step
    assert len(sys.argv) > 4, "No enough command line arguments\nArgs are: input_path ouput_path start stop [step]"
    input_path = os.path.expanduser(sys.argv[1])
    output_path = os.path.expanduser(sys.argv[2])
    assert os.path.exists(input_path), f"Cannot find file: {input_path}"
    cap = cv2.VideoCapture(input_path)
    assert cap.isOpened(), "Error occured opening the video file"
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc('m','p','4','v'), fps, (frame_width,frame_height))

    start = int(sys.argv[3])
    stop = int(sys.argv[4])
    step = 1
    if len(sys.argv) == 6:
        step = int(sys.argv[5])

    for i in range(start, stop, step):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if ret == True:
            out.write(frame)
        else:
            print(f"Error reading frame {i}.")
    cap.release()
    out.release()
