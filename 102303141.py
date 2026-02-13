import sys
import os
import yt_dlp
from moviepy.editor import VideoFileClip
from pydub import AudioSegment


# ----------------------------
# Download Videos
# ----------------------------
def download_videos(singer, num_videos):
    print("Downloading videos...")

    if not os.path.exists("videos"):
        os.makedirs("videos")

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'videos/%(id)s.%(ext)s',  # SAFE filename (video ID)
        'noplaylist': True,
        'quiet': False
    }

    search_query = f"ytsearch{num_videos}:{singer} songs"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])


# ----------------------------
# Convert Videos to Audio
# ----------------------------
def convert_to_audio(duration):
    print("Converting videos to audio...")

    if not os.path.exists("audios"):
        os.makedirs("audios")

    for file in os.listdir("videos"):
        video_path = os.path.join("videos", file)

        # Safe filename handling
        name = os.path.splitext(file)[0]
        audio_path = os.path.join("audios", name + ".mp3")

        try:
            clip = VideoFileClip(video_path)
            audio = clip.audio.subclip(0, duration)
            audio.write_audiofile(audio_path)
            clip.close()
        except Exception as e:
            print("Error converting:", file, e)


# ----------------------------
# Merge Audios
# ----------------------------
def merge_audios(output_file):
    print("Merging audios...")

    combined = AudioSegment.empty()

    for file in os.listdir("audios"):
        if file.endswith(".mp3"):
            audio_path = os.path.join("audios", file)
            sound = AudioSegment.from_mp3(audio_path)
            combined += sound

    combined.export(output_file, format="mp3")
    print("Mashup created successfully:", output_file)


# ----------------------------
# Main Function
# ----------------------------
def main():
    if len(sys.argv) != 5:
        print("Usage: python <roll>.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFile>")
        sys.exit(1)

    singer = sys.argv[1]

    try:
        num_videos = int(sys.argv[2])
        duration = int(sys.argv[3])
    except ValueError:
        print("NumberOfVideos and AudioDuration must be integers.")
        sys.exit(1)

    output_file = sys.argv[4]

    if num_videos <= 0 or duration <= 0:
        print("Values must be positive.")
        sys.exit(1)

    download_videos(singer, num_videos)
    convert_to_audio(duration)
    merge_audios(output_file)


if __name__ == "__main__":
    main()
