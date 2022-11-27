from cloudpathlib import CloudPath
from PIL import Image
import os.path
import s3fs

# Search within S3 Bucket and download
cp = CloudPath("s3://bucket-name/folder-path").download_to("")

# Resize images by 50%
for file in os.listdir('medical-images'):
    image = Image.open('medical-images/'+file)
    # You will have to create a folder called 'medical-images-scaled' or save within the same downloaded folder.
    image.resize((int(image.size[0] / 2), int(image.size[1] / 2))).save('medical-images-scaled/'{file}.scaled50)

# Upload resized folder to 'medical-images-scaled'
fs = s3fs.S3FileSystem().put("medical-images-scaled", "bucket-name/medical-images-scaled", recursive=True)
