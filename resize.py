import os
import io
from PIL import Image

def resize_images():
    directory = "/Users/bajkamalsingh/Desktop/Portfolio"
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(directory, filename)
            try:
                with Image.open(filepath) as img:
                    width, height = img.size
                    if max(width, height) > 1920:
                        ratio = 1920.0 / max(width, height)
                        new_size = (int(width * ratio), int(height * ratio))
                        img = img.resize(new_size, Image.Resampling.LANCZOS)
                        
                        # Save to memory first
                        img_format = img.format if img.format else ('JPEG' if filename.lower().endswith(('.jpg', '.jpeg')) else 'PNG')
                        buf = io.BytesIO()
                        img.save(buf, format=img_format)
                        
                        # Write raw bytes back to file (truncates, doesn't unlink)
                        with open(filepath, 'wb') as f:
                            f.write(buf.getvalue())
                        print(f"Resized {filename}")
            except Exception as e:
                print(f"Failed {filename}: {e}")

resize_images()
