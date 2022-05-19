if os.path.isdir(path):
    for l in os.listdir(rootDir):
        path1 = os.path.join(rootDir, l)

        if path1[len(path1) - 4:] == '.jpg':
            print(path1)
            if len(watermark) == 9:
                watermark_text(path1, path1,
                               text=watermark[-4:],
                               pos=(0, 0), color=text)
            if len(watermark) == 11:
                watermark_text(path1, path1,
                               text=watermark[-6:],
                               pos=(0, 0), color=text)
