from PIL import Image, ImageDraw, ImageFont
import os
from datetime import date, time, datetime


def watermark_text(input_image_path,
                   output_image_path,
                   text, image_path, color):
    photo = Image.open(input_image_path)
    drawing = ImageDraw.Draw(photo)
    black = color
    size=80

    font = ImageFont.truetype("arial.ttf", size)
    drawing.text((photo.width-len(text)*50, photo.height-size), text, fill=black, font=font)

    t = output_image_path.split('\\')
    if image_path:
        image_path = os.path.join(image_path, t[-1])
        photo.save(image_path)

    photo.save(output_image_path)

def watermark_text2(input_image_path,
                   output_image_path,
                   text, image_path, color):
    photo = Image.open(input_image_path)
    drawing = ImageDraw.Draw(photo)
    black = color
    size=80

    font = ImageFont.truetype("arial.ttf", size)
    drawing.text((photo.width-len(text)*50, photo.height-size), text, fill=black, font=font)

    t = output_image_path.split('\\')
    if image_path:
        image_path = os.path.join(image_path, t[-1])
        photo.save(image_path)
    output_image_path = output_image_path[:-4] + '-1.jpg'

    photo.save(output_image_path)



def InFolder(rootDir, watermark, image_path, text):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)


        if path[len(path) - 4:] == '.jpg':
            if len(watermark) == 9:
                watermark_text2(path, path,
                               text=watermark[-4:],
                               image_path=image_path, color=text)
            if len(watermark) == 11:
                watermark_text2(path, path,
                               text=watermark[-6:],
                               image_path=image_path, color=text)
        if os.path.isdir(path):
            for list in os.listdir(path):
                path1 = os.path.join(path, list)
                if path1[len(path1) - 4:] == '.jpg':
                    if len(watermark) == 9:
                        watermark_text(path1, path1,
                                       text=watermark[-4:],
                                       image_path=image_path, color=text)
                    if len(watermark) == 11:
                        watermark_text(path1, path1,
                                       text=watermark[-6:],
                                       image_path=image_path, color=text)


def TraverFolders(rootDir, watermark, type, text, image_path):


    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        t=1

        if os.path.isdir(path):
            typ=type.split(' ')
            for o in typ:
                if lists[0:3] == o:
                    watermark = lists
                    print('Обработка ', watermark)
                    f = open('log.txt', 'a')
                    d = datetime.now()
                    d_string = d.strftime("%d/%m/%Y   %H:%M:%S ")


                    f.write(d_string)
                    f.write(watermark)
                    f.write('\n')
                    f.close()
                    InFolder(path, watermark, image_path, text)

        if os.path.isdir(path):
            TraverFolders(path, watermark, type, text, image_path)

if __name__ == '__main__':
    n=0
    watermark = ' '

    with open("config.txt", 'r', encoding='utf-8') as f:
        config=f.read()
    f.close()
    config = config.split('\n')
    path = config[0]
    text=config[2]
    type=config[1]
    new_image=config[3]
    TraverFolders(path, watermark, type, text, new_image )

