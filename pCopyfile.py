__author__ = 'webon'

import os, shutil

# make sure that these directories exist
dir_src = "C:\\rossbai1\\"
dir_dst = "C:\\rossbai2\\"
for file in os.listdir(dir_src):
    src_file = dir_src+file
    dst_file = dir_dst+file
    #shutil.move(src_file, dst_file)
    shutil.copy(src_file, dst_file)
