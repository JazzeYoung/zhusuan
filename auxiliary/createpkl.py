#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cPickle as pk
from PIL import Image
import os
import time

import numpy as np
# input data path, output the file for the .pkl file
def main(path):
    print('Data path: %s' % path)
    train_images = [] # np.empty(1, 32*32)
    class_no = 0
    len_data = 0
    end_label = []
    dir_path = os.path.join(path, '/train')
    for classname in os.listdir(dir_path):
       class_no = class_no + 1
       file_path = os.path.join(dir_path, classname)
       for filename in os.listdir(file_path):
          len_data = len_data + 1
          img = Image.open(os.path.join(file_path, filename))
          img_array = np.asarray(img, dtype='float64') / 256
          train_images.append(np.ndarray.flatten(img_array))
       end_label.append(len_data)

    train_label = np.empty(len_data)
    for i in list(range(0, len_data)):
       for c in list(range(0, class_no)):
          if i > end_label[c]:
              continue
          else:
             train_label[i] = c
             break
    train_label = train_label.astype(np.int)
    
    write_file = open(os.path.join(path,'sar.pkl'), 'wb')
    pk.dump(train_images, write_file, -1)
    pk.dump(train_label, write_file, -1)

if __name__=='__main__':
    main(path)
