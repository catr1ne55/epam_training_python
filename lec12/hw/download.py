"""
Console utility to download images, process them, and save.

"""

import argparse
import os
import threading
from multiprocessing.pool import ThreadPool
import time
import requests
from PIL import Image

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILES = 0
ERRORS_COUNTER = 0
TOTAL_BYTES = 0
LOCK = threading.Lock()


def download_file(url, filepath, size):
    """
    Function to download image by its url.

    :param url: The URL with image to download.
    :type url: str
    :param filepath: New name of image, the path, where it will be saved.
    :type filepath: str
    :param size: Size of image after its processing.
    :type size: list
    :return: None
    """
    global TOTAL_BYTES
    global ERRORS_COUNTER
    global FILES
    print("Downloading from {}".format(url.strip()))
    try:
        response = requests.get(url)
        with LOCK:
            TOTAL_BYTES += len(response.content)
        img = Image.open(requests.get(url, stream=True).raw)
        img.thumbnail(size)
        img.convert('RGB').save(filepath, "JPEG")
        FILES += 1
        print("Done.")
    except Exception as e:
        print("An error: {}".format(e))
        with LOCK:
            ERRORS_COUNTER += 1


def get_images(url_file, directory, size):
    """
    Function to download images using file with urls.

    :param url_file: Path to file with URLs of images.
    :type url_file: str
    :param directory: Directory to save downloaded images.
    :type directory: str
    :param size: Size of image after its processing.
    :type size: str
    :return: None
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    size_list = [int(i) for i in size.split('x')]
    with open(url_file, 'r') as links:
        url_list = enumerate(links.readlines())
        size_of_urlfile = len(links.readlines())
    for url in url_list:
        save_as = str(url[0]).zfill(size_of_urlfile) + '.jpeg'
        download_file(url[1], os.path.join(directory, save_as), size_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download files by urls in file')

    parser.add_argument('filename', type=str, help='File with urls')
    parser.add_argument('--dir', type=str, default=CURRENT_DIR, help='Directory to save')
    parser.add_argument('--threads', type=int, default=1, help='Number of threads')
    parser.add_argument('--size', type=str, default='100x100', help='Size of the images to preview')

    args = parser.parse_args()

    if not os.path.exists(args.filename):
        raise FileExistsError("This file {} doesn't exist! Can't start downloading!".format(args.filename))

    thread_pool = ThreadPool(int(args.threads))
    start_time = time.time()
    thread_pool.apply(get_images, (args.filename, args.dir, args.size))
    total_time = time.time() - start_time
    thread_pool.close()
    thread_pool.join()

    print('-------')
    print("Downloaded {} images.".format(FILES))
    print("Downloaded {} bytes.".format(TOTAL_BYTES))
    print("{} errors occurred during downloading.".format(ERRORS_COUNTER))
    print("Total time: {:.3}".format(total_time))
