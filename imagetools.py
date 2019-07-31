from PIL import Image
import os
from aspect import calc_aspect_ratios

class ImageData:
    def __init__(self, name, height, width, image):
        self.name = name
        self.height = height
        self.width = width
        self.image = image
    
    def __str__(self):
        return f"{self.name} ({self.width}x{self.height})"

def _ensure_output_dir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)

def get_imagedata(filepath: str):
    image = Image.open(filepath)
    #for x in dir(image): print(x)
    return ImageData(os.path.basename(image.filename), image.height, image.width, image) 

def resize_to_aspect_ratios(filepath: str):
    img = get_imagedata(filepath)
    ratios = calc_aspect_ratios(img.width, img.height)

    output_dir =  os.path.join(os.path.dirname(filepath), "output")
    _ensure_output_dir(output_dir)

    for r in ratios:
        if r[0] < 300: continue
        output_path = os.path.join(output_dir, f"{img.name}_{r[0]}x{r[1]}.jpg")
        resized = img.image.resize(r)
        resized.save(output_path)
        print(f"wrote {output_path}")
