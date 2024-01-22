from PIL import Image

def process_cloud_image(image_path, output_path):
    # 打開圖片
    with Image.open(image_path) as img:
        # 轉換為RGBA模式（如果不是的話）
        img = img.convert("RGBA")

        # 加載像素數據
        pixels = img.load()

        # 遍歷每個像素
        for i in range(img.width):
            for j in range(img.height):
                r, g, b, a = pixels[i, j]

                # 判斷像素是否屬於雲（這裡需要自定義條件）
                if is_cloud_pixel(r, g, b):
                    # 設置雲的像素亮度為1（或其他需要的值）
                    pixels[i, j] = (r, g, b, 255)
                else:
                    # 設置非雲像素為透明
                    pixels[i, j] = (r, g, b, 0)

        # 保存處理後的圖片
        img.save(output_path)

def is_cloud_pixel(r, g, b):
    return r > 120 and g > 120 and b > 120  # 假設雲朵是非常亮的像素

# 使用函數
process_cloud_image('./inputImage/image.png', './outputImage/image1.png')
