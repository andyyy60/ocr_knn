#!/usr/bin/python2.7
import os, sys, cv2, exifread, time


def exif_info2time(ts):
    tpl = time.localtime(ts + 'UTC', '%Y:%m:%d %H:%M:%S%Z')
    return tpl


#finds images in "sample_images" folder
image_dir = os.getcwd()+"/sample_images/"

# printing original filenames:
# print "The dir is "+ str(os.listdir(dir))


# for filename in os.listdir(dir):
#     if '.JPG' in filename:
#          f = open(dir+filename, 'rb')
#          print exifread.process_file(f)

full_path = []
date = []

for filename in os.listdir(image_dir):
    f = open(image_dir + filename, 'rb')
    tags = exifread.process_file(f)
    for tag in tags.keys():
        if tag not in ('JPEGThumbnail', 'TIFFThumbnail'):  # these are not printable
            full_path.append(image_dir + filename) #appends full path
            times = tags['Image DateTime']
            temp = str(times).split()
            t = temp[0].split(':')
            time_and_date = "{0}-{1}-{2} {3}".format(t[0],t[1],t[2], temp[1])
            date.append(time_and_date)


total = []
for all in range(len(full_path)):
    temp = full_path[all] + ", " + date[all]
    print temp