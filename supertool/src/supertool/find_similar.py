import os
import hashlib


def compute_hash(file_path):
    """"This function returns the SHA-1 hash of the file

    :param file_path: Path to file
    :type file_path: str
    :return the hex representation of digest
    """

    h = hashlib.sha1()

    with open(file_path, 'rb') as file:
        chunk = 0
        while not chunk:
            chunk = file.read(1024)
            h.update(chunk)

    return h.hexdigest()


def find_similar(directory):
    """
    Finds similar files(by context) in given directory.

    :param directory: Path to target directory
    :type directory: str
    :return: dict with paths to similar files
    """
    if os.path.exists(directory):
        print("The given directory exists.")
        similar_files = {}
        for dirName, subdirs, fileList in os.walk(directory):
            print('Start scanning in {}'.format(dirName))
            print('...')
            for filename in fileList:
                path_to_file = os.path.join(dirName, filename)
                file_hash = compute_hash(path_to_file)
                if file_hash in similar_files:
                    similar_files[file_hash].append(path_to_file)
                else:
                    similar_files[file_hash] = [path_to_file]
        return similar_files
    else:
        raise Exception("This directory doesn't exist. Please try again with existing directory!")
