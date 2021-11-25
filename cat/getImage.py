import random
import requests
import shutil
import os
import atexit
import PIL.Image


def run():
    cats = [100, 101, 102, 200, 201, 202, 203, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 308, 400, 401, 402,
            403,
            404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 420, 421, 422, 423, 424, 425,
            426,
            429, 431, 444, 450, 451, 497, 498, 499, 500, 501, 502, 503, 504, 506, 507, 508, 509, 510, 511, 521, 523,
            525,
            599]  # the list of cats

    cat = random.choice(cats)  # get rand cat, split url
    url = f'https://http.cat/{cat}.jpg'
    filename = url.split("/")[-1]
    os.chdir('cat')  # changes working directory in order to store images in /cat

    r = requests.get(url, stream=True)
    if r.status_code == 200:  # if we can download successfully, we save the image
        r.raw.decode_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print(f"Successfully downloaded image {filename}")
    else:
        print("Could not download image")

    filesInDir = os.listdir(os.getcwd())
    filesToDelte = [file for file in filesInDir if file.endswith(".jpg")]

    def readsize():  # I assumed the images were not all the same size, but I am leaving this in
        global imgWidth, imgHeight
        img = PIL.Image.open(f'{cat}.jpg')
        imgWidth, imgHeight = img.size
        img.close()

    readsize()  # read image size

    def exitHandler():
        for file in filesToDelte:
            filePath = os.path.join(os.getcwd(), file)
            os.remove(filePath)

    atexit.register(exitHandler)