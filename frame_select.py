import cv2
import sys
import os

def show_frame(cap, frame_no):
    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    if (frame_no < 0) or (frame_no >= total_frames):
        print(f"While trying to select frame {frame_no}, video bounds exceeded. Video only has frames indices in range 0-{int(total_frames-1)}.")
        if frame_no < 0:
            frame_no = 0
        else:
            frame_no = total_frames-1
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
    ret, frame = cap.read()
    cv2.putText(frame, f"frame {int(frame_no)}", (50, 100), cv2.FONT_HERSHEY_DUPLEX, 2, (200, 230, 0), 2)
    if ret == True:
        cv2.imshow(f"{path}", frame)
    else:
        print(f"Error displaying frame {frame_no}.")
    return frame_no

if __name__ =='__main__':
    #check if video arg is correct
    assert len(sys.argv) > 1, "No video file path supplied command line argument"
    path = os.path.expanduser(sys.argv[1])
    assert os.path.exists(path), f"Cannot find file: {path}"
    cap = cv2.VideoCapture(path)
    assert cap.isOpened(), "Error occured opening the video file"

    key = None
    current_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
    skip_frame_size = 10
    cv2.namedWindow(f"{path}", cv2.WINDOW_NORMAL)
    while True:
        if key == ord('.'):
            current_frame+=1
        elif key == ord(','):
            current_frame-=1
        elif key == ord(']'):
            current_frame+=skip_frame_size
        elif key == ord('['):
            current_frame-=skip_frame_size
        elif key == ord('s'):
            skip_frame_size = int(input("Enter number of frames to use for skipping: "))
        elif key == ord('q'):
            break
        #show frame
        current_frame = show_frame(cap, current_frame)
        key=cv2.waitKey(0)

    cap.release()
    cv2.destroyAllWindows()