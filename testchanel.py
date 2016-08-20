import zipfile
zipped = zipfile.ZipFile((r'D:/AndroidTest.apk'), 'a', zipfile.ZIP_DEFLATED) 
empty_channel_file = "META-INF/mtchannel_{channel}".format(channel='testyk')
zipped.write((r'D:/empty'), empty_channel_file)