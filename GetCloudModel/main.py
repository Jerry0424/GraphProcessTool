from PIL import Image
def process_cloud_image(image_path, output_path):
    with Image.open(image_path) as img:
        img = img.convert("RGBA")
        pixels = img.load()
        for i in range(img.width):
            for j in range(img.height):
                r, g, b, a = pixels[i, j]
                if is_cloud_pixel(r, g, b):
                    pixels[i, j] = (r, g, b, 255)
                else:
                    pixels[i, j] = (r, g, b, 0)
        img.save(output_path)

def is_cloud_pixel(r, g, b):
    return r > 100 and g > 100 and b > 100

process_cloud_image('./inputImage/image5.png', './outputImage/image5.png')