import os
import time
import datetime

import cv2

import config


def get_log():
    """Get a specific number of the last lines of the log file."""
    log_path = config.Config.LOG_FILE_PATH
    nr_lines = config.Config.NR_DISPLAY_LOG_LINES
    log_text = None
    try:
        with open(log_path, "r") as file:
            log_text = list(file)[-nr_lines:]
    except FileExistsError:
        pass

    return log_text


def save_image_from_camera():
    """Save images from camera to a directory."""
    # Create a directory to save images
    dt_string = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
    save_dir = config.Config.IMAGE_SAVE_PATH
    save_dir = os.path.join(save_dir, dt_string)
    os.makedirs(save_dir, exist_ok=True)

    video_cap = cv2.VideoCapture(0)
    video_fps = video_cap.get(cv2.CAP_PROP_FPS)
    nr_frames = 0
    frame_offset = video_fps / config.Config.IMAGE_FPS
    while video_cap.isOpened():
        ret, image = video_cap.read()
        if image is not None:
            if nr_frames % frame_offset == 0:
                image_path = str(time.time()) + '.jpg'
                image_path = os.path.join(save_dir, image_path)
                cv2.imwrite(image_path, image)
                cv2.imwrite(config.Config.IMAGE_FILE_PATH, image)

            nr_frames = (nr_frames + 1) % frame_offset

    video_cap.release()
