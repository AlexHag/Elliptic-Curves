from PIL import Image
import os

def add_white_border(in_path, out_path, width, height, extra_pad_top):
    image = Image.open(in_path)

    new_size = (image.width + 2 * width, image.height + 2 * height + extra_pad_top)
    new_image = Image.new("RGB", new_size, "white")
    new_image.paste(image, (width, height + extra_pad_top))
            
    # Save the new image
    new_image.save(out_path)

in_dir = "edwards_curve_images"
if not os.path.exists(in_dir):
        os.makedirs(in_dir)

out_dir = "edwards_curve_images_padded"
if not os.path.exists(out_dir):
        os.makedirs(out_dir)

for filename in os.listdir(in_dir):
    arr = filename.split("_")
    new_name = ""
    if (filename.startswith("cool")):
        new_name = "edwards_curve_prime_" + arr[5]
    else:
        new_name = "edwards_curve_prime_" + arr[4]
    add_white_border(f"{in_dir}/{filename}", f"{out_dir}/{new_name}", 200, 300, 150)
