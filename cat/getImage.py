import random
import os
import atexit


def run():
    filesInDir = os.listdir(os.getcwd())
    filesToDelte = [file for file in filesInDir if file.endswith(".jpg")]

    def exitHandler():
        for file in filesToDelte:
            filePath = os.path.join(os.getcwd(), file)
            os.remove(filePath)

    atexit.register(exitHandler)


def getCat():
    cats = [100, 101, 102, 200, 201, 202, 203, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 308, 400, 401, 402,
            403,
            404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 420, 421, 422, 423, 424, 425,
            426,
            429, 431, 444, 450, 451, 497, 498, 499, 500, 501, 502, 503, 504, 506, 507, 508, 509, 510, 511, 521, 523,
            525,
            599]  # the list of cats

    os.chdir('cat')
    cat = random.choice(cats)
    print(cat)
    return cat
