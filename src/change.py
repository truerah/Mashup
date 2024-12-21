from pydub import AudioSegment
import os
import argparse

def audioconv(vid_dir):
    os.makedirs(f"{vid_dir}_aud")
    aupaths=[]
    for vfile in os.listdir(vid_dir):
        if vfile.endswith(".mp4"):
            bname=os.path.splitext(vfile)[0]
            aufile=os.path.join(f"{vid_dir}_aud",f"{bname}.mp3")
            vpath=os.path.join(vid_dir,vfile)

            try:
                aud=AudioSegment.from_file(vpath,format='mp4')
                aud.export(aufile,format='mp3')
                aupaths.append(aufile)
                print(f"Converted {vfile} to {aufile}")
            except Exception as e:
                print(f"Error converting to mp3 {e}")
    return aupaths

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert video files to MP3.")
    parser.add_argument("vid_dir", help="Directory containing video files")

    args = parser.parse_args()
    audioconv(args.vid_dir)

# audioconv("laroi_videos")