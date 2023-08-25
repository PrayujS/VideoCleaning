from moviepy.editor import VideoFileClip

clip1 = VideoFileClip("input video")
# Clip Trimming
start_time = 3.3
end_time = 16.7
trimmed_clip1 = clip1.subclip(start_time, end_time)

width, height = trimmed_clip1.size
print(width, height )

file_name = 'TrimmedVideo.mp4'

trimmed_clip1.write_videofile(file_name, codec='libx264')


