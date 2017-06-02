#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cPickle as pk
from PIL import Image
import os
import time

import numpy as np

# input image subpath create a images matrix( each row is one image flattened)

def imageflatten(path):
    images = []
    class_no = 0
    len_data = 0
    end_label = []
    for classname in os.listdir(path):
       class_no = class_no + 1
       file_path = os.path.join(path, classname)
       for filename in os.listdir(file_path):
#          print len_data
          flist = filename.split('.')
          if len(flist) > 1:
             if(flist[1]=='jpg' or flist[1]=='png'):
                len_data = len_data + 1
                img = Image.open(os.path.join(file_path, filename))
                img_array = np.asarray(img, dtype='float64') / 256
                images.append(np.ndarray.flatten(img_array))
             else:
                pass
          else:
             pass
       end_label.append(len_data)
       print len_data
       print 'Segmentation:-----------%d-----------------' % end_label.__len__()

    images = np.array(images)
    labels = np.empty(len_data)
    for i in list(range(0, len_data)):
       for c in list(range(0, class_no)):
          if i > end_label[c]:
              continue
          else:
             labels[i] = c
             break
    labels = np.array(labels)
    labels = labels.astype(np.int)
    return images, labels
# input data path, output the file for the .pkl file
"""
    Input data from path 
"""
def main(path):
    print('Data path: %s' % path)
    train_images, train_label = imageflatten(os.path.join(path, 'train'))
    print 'train images: %d' % train_label.size
    test_images, test_label = imageflatten(os.path.join(path, 'test'))
    print 'test images: %d' % test_label.size
#    train_images = [] # np.empty(1, 32*32)
#    class_no = 0
#    len_data = 0
#    end_label = []
#    dir_path = os.path.join(path, 'train')
#    for classname in os.listdir(dir_path):
#       class_no = class_no + 1
#       file_path = os.path.join(dir_path, classname)
#       for filename in os.listdir(file_path):
##          print len_data
#          flist = filename.split('.')
#          if len(flist) > 1:
#             if(flist[1]=='jpg' or flist[1]=='png'):
#                len_data = len_data + 1
#                img = Image.open(os.path.join(file_path, filename))
#                img_array = np.asarray(img, dtype='float64') / 256
#                train_images.append(np.ndarray.flatten(img_array))
#             else:
#                pass
#          else:
#             pass
#       end_label.append(len_data)
#       print len_data
#       print 'Segmentation:-----------%d-----------------' % end_label.__len__()
#
#    train_images = np.array(train_images)
#    train_label = np.empty(len_data)
#    for i in list(range(0, len_data)):
#       for c in list(range(0, class_no)):
#          if i > end_label[c]:
#              continue
#          else:
#             train_label[i] = c
#             break
#    train_label = np.array(train_label)
#    train_label = train_label.astype(np.int)
#    print train_label.size
    write_file = open(os.path.join(path,'cifar.pkl'), 'wb')
    pk.dump(train_images, write_file, -1)
    pk.dump(train_label, write_file, -1)
    pk.dump(test_images, write_file, -1)
    pk.dump(test_label, write_file, -1)


if __name__=='__main__':
    path = './cifar10/'
    main(path)
