from pytube import YouTube

# Replace 'your_video_url' with the actual URL of the YouTube video you want to download
video_url = 'your_video_url'

try:
    # Creating a YouTube object
    yt = YouTube('https://www.youtube.com/watch?v=0mCVpUDCkEk&list=RDGMEMCMFH2exzjBeE_zAHHJOdxgVM4tywp83zkmk&index=3')

    # Accessing the video stream with the highest resolution
    video_stream = yt.streams.get_highest_resolution()

    # Downloading the video
    print(f"Downloading: {yt.title}...")
    video_stream.download()
    print("Download complete!")

except Exception as e:
    print(f"An error occurred: {e}")




