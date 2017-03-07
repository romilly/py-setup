import os
from os.path import join, getsize

import shutil

def process(old_dir, new_dir):
        # zap existing converted content
        zap_target_dir(new_dir)
        os.mkdir(new_dir)
        convert(old_dir, new_dir)

def convert(old_dir, new_dir):
    for root, dirs, files in os.walk(old_dir):
        print(root)
        for directory in dirs:
            os.mkdir(os.path.join(new_dir,directory))
        # print(sum(getsize(join(root, name)) for name in files), end=" ")
        # print("bytes in", len(files), "non-directory files")
        # if 'CVS' in dirs:
        #     dirs.remove('CVS')  # don't visit CVS directories


def zap_target_dir(new_dir):
    if os._exists(new_dir):
        shutil.rmtree(new_dir)

process('q2w2','new_q2w2')
