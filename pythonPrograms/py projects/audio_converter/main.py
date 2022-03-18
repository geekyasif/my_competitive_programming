import moviepy.editor
from tkinter.filedialog import *

#opening file
video = askopenfilename()

#taking video to read
video = moviepy.editor.VideoFileClip(video)

# extracting audio from video
audio = video.audio

# saving the audio file
audio.write_audiofile("sample.mp3")

#done
print("Completed")