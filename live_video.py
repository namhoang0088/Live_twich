import subprocess
import os

def start_stream(stream_key, video_path):
    command = [
        'ffmpeg', 
        '-re',
        '-stream_loop', '-1', 
        '-i', video_path,
        '-c:v', 'libx264', 
        '-preset', 'fast', 
        '-b:v', '2500k', 
        '-maxrate', '2500k', 
        '-bufsize', '5000k', 
        '-pix_fmt', 'yuv420p', 
        '-g', '60', 
        '-c:a', 'aac', 
        '-b:a', '160k', 
        '-ac', '2', 
        '-ar', '44100', 
        '-f', 'flv', 
        'rtmp://live.twitch.tv/app/' + stream_key
    ]
    return subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def start_stream_cycle(stream_key, video_paths):
    concatenated_video_path = 'concatenated_video.mp4'
    start_stream(stream_key, concatenated_video_path)

if __name__ == "__main__":
    twitch_stream_key = 'live_1039732177_WR5stX7IiA7bofMUVQyijQKgFRhziY'  # Thay đổi 'YOUR_TWITCH_STREAM_KEY' bằng stream key của bạn
    video_paths = ['input1.mp4']  # Danh sách các đường dẫn đến các video bạn muốn stream
    start_stream_cycle(twitch_stream_key, video_paths)


    