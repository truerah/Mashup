from pydub import AudioSegment
import os
import argparse

def merging(cut_aupaths_dir, output_file):
    merged_dir = f"{cut_aupaths_dir}_merged"
    os.makedirs(merged_dir, exist_ok=True)

    combaud = AudioSegment.empty()

    for cutfile in os.listdir(cut_aupaths_dir):
        cutfile_path = os.path.join(cut_aupaths_dir, cutfile)
        if cutfile.endswith(".mp3"):
            try:
                aud = AudioSegment.from_file(cutfile_path)
                combaud += aud
            except Exception as e:
                print(f"Error merging: {e}")

    # Save the final merged file inside the merged folder
    output_path = os.path.join(merged_dir, output_file)
    try:
        combaud.export(output_path, format='mp3')
        print(f"Merged audio saved as: {output_path}")
    except Exception as e:
        print(f"Failed to save: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge audio files.")
    parser.add_argument("cut_aupaths_dir", help="Directory containing cut audio files")
    parser.add_argument("output_file", help="Output filename for merged audio")

    args = parser.parse_args()
    merging(args.cut_aupaths_dir, args.output_file)
    

# merging("laroi_videos_aud_cut")
