import sys
import os
from imagetools import ImageData, get_imagedata, resize_to_aspect_ratios

def _is_image_file(filename: str):
    return filename.lower().endswith(".jpg") or filename.lower().endswith(".png")


def find_images_in_dir(dirpath):
    return [os.path.join(dirpath,f) for f in os.listdir(dirpath) if _is_image_file(f) ]
    
def show_image_data(imgpath: str):
    print(get_imagedata(imgpath))


def main(path: str, print_only: bool = False):
    img_paths = []

    if not os.path.isabs(path):
        path = os.path.abspath(path)

    if not os.path.exists(path):
        print(f"Error: {path} does not exist.")

    if os.path.isdir(path):
        img_paths.extend(find_images_in_dir(path))
    else:
        img_paths.append(path)
    
    if print_only:
        show_image_data(path)
    else:
        for img_path in img_paths:
            resize_to_aspect_ratios(img_path)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("resizer.py <img or dir path> [--show]")
        sys.exit(1)
    
    path = sys.argv[1]
    print_only = len(sys.argv) > 2 and sys.argv[2] == "--show"

    main(path, print_only)

