import os
import numpy as np
import skvideo
import skvideo.io
from moviepy import editor
from tempfile import TemporaryDirectory



def resize_video_clip(file_path, resized_file_path):
    with editor.VideoFileClip(file_path) as clip:
        resized_clip = clip.resize((100,100))
        resized_clip.write_videofile(resized_file_path, verbose=False, logger=None)
    return resized_file_path


def convert_video_to_numpy_array(file_path):
    return skvideo.io.vread(file_path)


def extract_frames_from_video_array(video_array):   
    frames = video_array.shape[0]
   
    if frames == 40:
        return video_array

    mid_frame = frames // 2

    clip_1 = video_array[:10]
    clip_2 = video_array[mid_frame-10:mid_frame+10]
    clip_3 = video_array[-10:]

    extracted_clips = [clip_1, clip_2, clip_3]
    new_video = extracted_clips[0]

    for clip in extracted_clips[1:]:
        new_video = np.vstack((new_video, clip))

    return new_video


def preprocess_video(file_path):

    with TemporaryDirectory() as temp_dir:
        file_name = os.path.basename(file_path)
        temp_file_path = os.path.join(temp_dir, file_name)
        resized_video = resize_video_clip(file_path, temp_file_path)
        video_array = convert_video_to_numpy_array(resized_video)
    
    extracted_frames = extract_frames_from_video_array(video_array)
    batch = np.expand_dims(extracted_frames, axis=0)
    return batch


