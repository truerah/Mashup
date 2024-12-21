from pydub import AudioSegment
import os
import argparse

def audiocut(aud_dir, cut_duration):
    cut_dir = f"{aud_dir}_cut"
    os.makedirs(cut_dir, exist_ok=True)
    
    cut_audpaths = []
    for aufile in os.listdir(aud_dir):
        input_path = os.path.join(aud_dir, aufile)
        if aufile.endswith(".mp3"):
            cutted_path = os.path.join(cut_dir, f"{os.path.splitext(aufile)[0]}_cut.mp3")
            try:
                AudioSegment.from_file(input_path)[:cut_duration * 1000].export(cutted_path, format='mp3')
                cut_audpaths.append(cutted_path)
                print(f"Cut {cutted_path}")
            except Exception as e:
                print(f"Error processing {input_path}: {e}")
    
    return cut_audpaths

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cut audio files to a specific duration.")
    parser.add_argument("aud_dir", help="Directory containing audio files")
    parser.add_argument("cut_duration", type=int, help="Duration in seconds to cut the audio files")

    args = parser.parse_args()
    audiocut(args.aud_dir, args.cut_duration)
# audiocut("laroi_videos_aud", 6)
