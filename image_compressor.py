import PIL
from PIL import Image
import os

my_width = 2000
source_dir = 'D:\project-\Images'
destination_dir = 'D:\project-\After compress'


def resize_img(old_img,new_img,my_width):
    img = Image.open(old_img)
    wpercent = (my_width/float(img.size[0]))
    hsize = int ((float(img.size[1])*float(wpercent)))
    img = img.resize((my_width,hsize), PIL.Image.ANTIALIAS)
    img.save(new_img)

def entire_dir(source_dir,destination_dir,my_width):
    files = os.listdir(source_dir)


    i=0
    for file in files:
        i=i+1
        old_img = source_dir + "/" + file
        new_img = destination_dir + "/" + file

        resize_img(old_img,new_img,my_width)
        print("Done Image",i)

entire_dir(source_dir,destination_dir,my_width)