# Video Util Docs

## Environment Setup
A Conda enviroment file is provided to set up the environment for the video tools. To use the environment, simply enter the following commands in the same folder as the `conda_environment.yml` file:

```
conda env create -f conda_environment.yaml
```

Whenever you want to use the video tools, you can activate the environment using the command:

```
conda activate video_tools
```

## Frame Select Tool
This tool can be used to view the frame number of a video. To open a video simply supply the path to the video file as an argument to the select python file.

For example:
```
python frame_select.py ~/Desktop/my_video.mp4
```

This will open the video in a window, currently the following commands are available:

| key | command            |
|-----|--------------------|
| .   | forward 1 frame    |
| ,   | back 1 frame       |
| ]   | forward n frames   |
| [   | back n frames      |
| s   | set n (default 10) |
| q   | quit               |

## Video Clipping Tool

This tool allows you to extract frames from a video easily. The command is used as follows:

```
python clip_video.py input_path output_path start stop [step]
```

The `input_path` and `output_path` are the locations of the video files and `start` `stop` and `step` are the starting frame, end frame where step is the size of the jump between frames. The `step` parameter is optional.