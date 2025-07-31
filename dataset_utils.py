import argparse
import os
import shutil
from PIL import Image 

def rename_files(directory):
    for count, filename in enumerate(os.listdir(directory)):
        dst = f"{str(count)}.jpg"
        src = f"{directory}/{filename}"
        dst = f"{directory}/{dst}"
        os.rename(src, dst)

def reduce_image_res(input_pth, output_pth, new_width, new_height):
    try: 
        img = Image.open(input_pth)
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        resized_img.save(output_pth)
        print(f"image resolution saved to {output_pth}")

    except FileNotFoundError:
        print(f"file {input_pth} not found")
    except Exception as e:
        print(f"an error has occured: {e}") 

parser = argparse.ArgumentParser()
parser.add_argument("com", type=str, help="command to run")
parser.add_argument("directory", type=str, help="location of target directory")
parser.add_argument("output", type=str, help="location of output directory")
opt = parser.parse_args()

com = opt.com
dir = opt.directory
out = opt.output
if com == "enumerate":
    rename_files(dir)
elif com == "resize":
    reduce_image_res(dir, out, 800, 800)


