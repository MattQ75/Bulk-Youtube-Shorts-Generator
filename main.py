from moviepy.editor import VideoFileClip, TextClip,ImageClip,AudioFileClip,CompositeVideoClip
from moviepy.config import change_settings
import csv
import random
import re
import time




def extract_number_onpath(path):
    match = re.search(r'\\(\d+)-\d+.csv$', path)
    if match:
        numero = int(match.group(1))
        return numero
    else:
        return None


#       Windows

video = VideoFileClip("C:\\Users\\Matteo\\Dropbox\\Matteo\\python_exp\\Files\\background.mp4")
like_path = "C:\\Users\\Matteo\\Dropbox\\Matteo\\python_exp\\Files\\like.png"
subscribe_path = "C:\\Users\\Matteo\\Dropbox\\Matteo\\python_exp\\Files\\subscribe.png"
audio_path = "C:\\Users\\Matteo\\Dropbox\\Matteo\\python_exp\\Files\\audio.mp3"
file_path_csv = "C:\\Users\\Matteo\\Dropbox\\Matteo\\python_exp\\input_csv\\1-50.csv"
number_check = extract_number_onpath(file_path_csv)
csv_output_file = "C:\\Users\\Matteo\\Dropbox\\Matteo\\python_exp\\output_csv\\1-50.csv"


#       MacoS

# change_settings({"IMAGEMAGICK_BINARY": "/Applications/ImageMagick-7.0.10/bin/convert"})
# video = VideoFileClip("/Users/matteoscarcella/Dropbox/Matteo/python_exp/Files/background.mp4")
# like_path = "/Users/matteoscarcella/Dropbox/Matteo/python_exp/Files/like.png"
# subscribe_path = "/Users/matteoscarcella/Dropbox/Matteo/python_exp/Files/subscribe.png"
# audio_path = "/Users/matteoscarcella/Dropbox/Matteo/python_exp/Files/audio.mp3"
# file_path_csv = "/Users/matteoscarcella/Dropbox/Matteo/python_exp/input_csv/1-50.csv"
# csv_output_file = "/Users/Matteo/Dropbox/Matteo/python_exp/output_csv/1-50.csv"



like = (  ImageClip(like_path)
             .set_position(("center", 0.05), relative=True)
             .set_duration(9.8)
             .set_start(5.3)
)
suscribe = (  ImageClip(subscribe_path)
             .set_position(("center", 0.9), relative=True)
             .set_duration(9.8)
             .set_start(5.3)
)
audio = (   AudioFileClip(audio_path)
             .set_start(0)
             .set_duration(15.1)
)

video.set_audio(audio)


def perc_csv():
    with open(file_path_csv,'r') as csvinput:
        with open(csv_output_file, 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)

            all = []
            row = next(reader)

            row.append('p1-')            
            row.append('p2+')
            row.append('p3-')            
            row.append('p4+')
            all.append(row)
            for row in reader:
                p1_value_write, p2_value_write,p3_value_write,p4_value_write = perc_gen()
                row.append(p1_value_write)
                row.append(p2_value_write)
                row.append(p3_value_write)
                row.append(p4_value_write)         
                all.append(row)
            writer.writerows(all)


def perc_gen():
    p1_value_write = random.randint(1, 50)
    p2_value_write = 100 - p1_value_write

    p3_value_write = random.randint(1, 50)
    p4_value_write = 100 - p3_value_write

    p1_value_write = str(p1_value_write) + "%"
    p2_value_write = str(p2_value_write) + "%"
    p3_value_write = str(p3_value_write) + "%"
    p4_value_write = str(p4_value_write) + "%"
    return p1_value_write,p2_value_write,p3_value_write,p4_value_write


def format_text(txt1,txt2):
    l1 = len(txt1)
    l2 = len(txt2)
    for i in range(l1):
        if (i%21 == 0):
            text1_edited = txt1[:i] + "\n" + txt1[i:]
    for i in range(l2):
        if (i%21 == 0):
            text2_edited = txt2[:i] + "\n" + txt2[i:]
    return text1_edited, text2_edited

def download_video(result, path, fps):
    result.write_videofile(path, fps=fps)

def create_bulk_videos():
    with open(csv_output_file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for i, row in enumerate(csv_reader, start=1):
            
            text1_value = row['Text1']
            text2_value = row['Text2']
            p1_value_read = row['p1-']
            p2_value_read = row['p2+']

            text3_value = row['Text3']
            text4_value = row['Text4']
            p3_value_read = row['p3-']
            p4_value_read = row['p4+']
            text1_value,text2_value,text3_value,text4_value = format_text(text1_value,text2_value,text3_value,text4_value)
            txt_1 = ( TextClip(text1_value,font="Segoe-UI-Bold",fontsize=81,color='white', stroke_color='black', stroke_width=3)
                .set_position(("center", 0.2), relative=True)
                .set_duration(14.1)
                .set_start(0.5)
                .fadein(0.5)
            )
            txt_2 = ( TextClip(text2_value,font="Segoe-UI-Bold",fontsize=81,color='white', stroke_color='black', stroke_width=3)
                        .set_position(("center", 0.7), relative=True)
                        .set_duration(12.8)
                        .set_start(2.3)
                        .fadein(0.5)
            )
            perc_1 = ( TextClip(p1_value_read,font="Segoe-UI-Bold",fontsize=81,color='#FF3630', stroke_color='#800400', stroke_width=2)
                        .set_position(("center", 0.35), relative=True)
                        .set_duration(3.1)
                        .set_start(12)
                        .fadein(0.3)
            )
            perc_2 = ( TextClip(p2_value_read,font="Segoe-UI-Bold",fontsize=81,color='#7ED957', stroke_color='#216d00', stroke_width=2)
                        .set_position(("center", 0.6), relative=True)
                        .set_duration(3.1)
                        .set_start(12)
                        .fadein(0.3)
            )

            txt_3 = ( TextClip(text3_value,font="Segoe-UI-Bold",fontsize=81,color='white', stroke_color='black', stroke_width=3)
                .set_position(("center", 0.2), relative=True)
                .set_duration(14.1)
                .set_start(0.5)
                .fadein(0.5)
            )
            txt_4 = ( TextClip(text4_value,font="Segoe-UI-Bold",fontsize=81,color='white', stroke_color='black', stroke_width=3)
                        .set_position(("center", 0.7), relative=True)
                        .set_duration(12.8)
                        .set_start(2.3)
                        .fadein(0.5)
            )
            perc_3 = ( TextClip(p3_value_read,font="Segoe-UI-Bold",fontsize=81,color='#FF3630', stroke_color='#800400', stroke_width=2)
                        .set_position(("center", 0.35), relative=True)
                        .set_duration(3.1)
                        .set_start(12)
                        .fadein(0.3)
            )
            perc_4 = ( TextClip(p4_value_read,font="Segoe-UI-Bold",fontsize=81,color='#7ED957', stroke_color='#216d00', stroke_width=2)
                        .set_position(("center", 0.6), relative=True)
                        .set_duration(3.1)
                        .set_start(12)
                        .fadein(0.3)
            )


            number_check = extract_number_onpath(csv_output_file)
            print(number_check, i)
            time.sleep(5)
            result = CompositeVideoClip([video, txt_1, txt_2,suscribe,like,perc_1,perc_2]).set_audio(audio)
            #       Windows
            path_output_video = "C:\\Users\\Matteo\\Dropbox\\Matteo\\python_exp\\videos\\" + str(i + number_check) + ".mp4"
            #       MacOS
            # path_output_video = "/Users/matteoscarcella/Dropbox/Matteo/python_exp/videos/" + str(i + number_check) + ".mp4"

            download_video(result,path_output_video,30)


perc_csv()
#create_bulk_videos()