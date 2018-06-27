import os
import time

file_path = "/home/mufeed/Desktop/La.Casa.de.Papel.S01E05.720p.NF.WEB-DL.Pahe-LavinMovie.mkv"
previous_size = 0
while True:
    if os.path.isfile(file_path):
        size = os.stat(file_path)
        current_size = size.st_size
        speed = (current_size - previous_size)/1024
        print("downloaded : "+str(current_size/(1024*1024))+"Mb, speed :",str(speed)+" kb/sec")
        previous_size = current_size
        time.sleep(1)
