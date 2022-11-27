import s3fs
from cloudpathlib import CloudPath
from PIL import Image
import os.path

# Download image folder
cp = CloudPath("s3://bucket-name").download_to("")

# Resize
for file in os.listdir('medical-images'):
    image = Image.open('medical-images/'+file)
    # You will have to create a folder called 'medical-images-scaled' or save within the same downloaded folder.
    image.resize((int(image.size[0] / 2), int(image.size[1] / 2))).save('medical-images-scaled/'+file)

# Upload resized folder
fs = s3fs.S3FileSystem().put("medical-images-scaled", "bucket-name/medical-images-scaled", recursive=True)
