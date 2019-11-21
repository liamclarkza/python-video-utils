import cv2
import sys
import os

if __name__ =='__main__':
    # check if video arg is correct
    # input_path ouput_path start stop step
    assert len(sys.argv) > 3, "No enough command line arguments\nArgs are: output_video_path video_1_path video_2_path [video_3_path...]"
    output_path = os.path.expanduser(sys.argv[1])
    input_paths = []
    for i in range(2, len(sys.argv)):
        input_path = os.path.expanduser(sys.argv[i])
        assert os.path.exists(input_path), f"Cannot find file: {input_path}"
        input_paths.append(input_path)
    
    
    print(f"Joining videos:\n{input_paths}\nOutput to:\n{output_path}")

    cap = cv2.VideoCapture(input_paths[0])
    assert cap.isOpened(), "Error occured opening the video file"
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc('m','p','4','v'), fps, (frame_width,frame_height))
    
    for i, input_path in enumerate(input_paths):
        if i>0:
            cap = cv2.VideoCapture(input_path)
            assert cap.isOpened(), "Error occured opening the video file"
            assert (frame_width == int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))) and \
                (frame_height == int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))), \
                    f"Dimensions for {input_path} don't match {input_paths[0]}"

        for i in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
            cap.set(cv2.CAP_PROP_POS_FRAMES, i)
            ret, frame = cap.read()
            if ret == True:
                out.write(frame)
            else:
                print(f"Error reading frame {i}.")
                quit()
        cap.release()
    out.release()
