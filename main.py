# import argparse
# import os
# from downloadder import downvid
# from Converterr import audioconv
# from Merger import merging
# from cutter import audiocut
# from zipsend import zip_and_email_folder

import os
import argparse

def main(singername, number, duration, output_file, email):
  
    os.system(f"python downloadder.py {singername} {number}")


    os.system(f"python Converterr.py {singername}_videos")

  
    os.system(f"python cutter.py {singername}_videos_aud {duration}")


    os.system(f"python Merger.py {singername}_videos_aud_cut {output_file}")

    
    os.system(f"python zipsend.py {singername}_videos_aud_cut_merged {email}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("singername")
    parser.add_argument("number", type=int)
    parser.add_argument("duration", type=int)
    parser.add_argument("output_file")
    parser.add_argument("email")

    args = parser.parse_args()
    main(args.singername, args.number, args.duration, args.output_file, args.email)
