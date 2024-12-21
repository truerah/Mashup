import yt_dlp
import argparse
import os

def downvid(singername, number):
    search_query = f"ytsearch{number}:{singername}"
    download_dir = f"{singername}_videos"
    os.makedirs(download_dir, exist_ok=True)

    ydl_opts = {
        'format': 'mp4',
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'noplaylist': True,  # Ensure only single videos are downloaded
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([search_query])
            print(f"Downloaded {number} videos for {singername}")
        except Exception as e:
            print(f"Error downloading videos: {str(e)}")

    return download_dir

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download videos using yt_dlp.")
    parser.add_argument("singername", help="Name of the singer or artist")
    parser.add_argument("number", type=int, help="Number of videos to download")

    args = parser.parse_args()
    downvid(args.singername, args.number)
# downvid("laroi",2)