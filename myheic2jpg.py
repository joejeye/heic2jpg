from PIL import Image
from pillow_heif import register_heif_opener
import os
import argparse
import re

'''
Convert one heic file to the jpg file
'''
def convertOneImage(input_img: str, output_img: str, quality: int) -> None:
    image = Image.open(input_img)
    image.convert('RGB').save(output_img, quality=quality)
    print(f"Successfully converted image '{input_img}'")


'''
Convert all heic files from the input directory
to the jpg files in the output directory
'''
def batchConvert(input_dir: str, output_dir: str, quality) -> None:
    # Check if output directory exists. If not create one.
    if not os.path.isdir(output_dir):
        print(f"Output directory '{output_dir}' does not exist. Creating one.")
        try:
            os.mkdir(output_dir)
            print(f"Output directory '{output_dir}' created successfully.")
        except FileNotFoundError:
            print(f"Cannot create directory '{output_dir}'. Parent directory does not exist.")

    # Get the list of heic file names from the input directory
    file_list = [
        f for f in os.listdir(input_dir)
        if (f.endswith('.heic') or f.endswith('.HEIC'))
    ]

    # Convert each heic file to the jpg file
    for file in file_list:
        input_img = os.path.join(input_dir, file)
        output_img = os.path.join(output_dir, re.sub(r"[.]\w+$", r".jpg", file))
        convertOneImage(input_img, output_img, quality)


if __name__ == "__main__":
    # Parse input arguments from the CLI
    parser = argparse.ArgumentParser(
        prog='JoeJeye`s program',
        description='Convert heic files to jpg files',
        epilog='The arguments for -i and -o must either both be file names or directory names'
    )
    parser.add_argument("-i", "--input", default="", type=str,
                        help="The input heic file name or the input directory name")
    parser.add_argument("-o", "--output", default="", type=str,
                        help="The output heic file name or the output directory name")
    parser.add_argument("-q", "--quality", default=95, type=int,
                        help="The saved image quality between 1 (worst) and 95 (best, default)")
    
    args = parser.parse_args()

    # Determin saved image quality
    q = args.quality
    if q < 1:
        q = 1
    elif q > 95:
        q = 95

    # To use Pillow HEIF extension
    register_heif_opener()
    
    if os.path.isdir(args.input):
        batchConvert(args.input, args.output, q)
    else:
        convertOneImage(args.input, args.output, q)