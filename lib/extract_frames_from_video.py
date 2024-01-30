import cv2
import os
import argparse
from tqdm import tqdm

class ExtractFramesFromVideo:
    def __init__(self, video_path):
        self.video_path = video_path

        assert os.path.exists(video_path), "{} don't exists".format(video_path)

        os.makedirs(os.path.join(os.path.dirname(video_path), f'frames/{os.path.basename(video_path)}'), exist_ok=True)
        self.output_path = os.path.join(os.path.dirname(video_path), f'frames/{os.path.basename(video_path)}')

        assert os.path.exists(self.output_path), "{} don't exists".format(self.output_path)

    def extract_frames(self):
        cap = cv2.VideoCapture(self.video_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        progress = tqdm(total=total_frames)

        count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                cv2.imwrite(f"{self.output_path}/frame_{count}.jpg", frame)
                count += 1
                progress.update(1)
            else:
                break

        cap.release()
        progress.close()

if __name__ == '__main__':
    args = argparse.ArgumentParser(description='Extract frames from video')
    args.add_argument('--video_path', type=str, help='Path do video', default='D:\Projetos\orto\DJI_0358.mp4')
    args = args.parse_args()

    ExtractFramesFromVideo(args.video_path, args.frame_rate).extract_frames()