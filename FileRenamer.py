import os
import subprocess
import sys

def get_valid_filename(directory, filename, extention, index):
    if  index == 0:
        strIndex = ""
    else:
        strIndex = " (" + str(index) + ")"

    newFilename = filename + strIndex + extention

    if os.path.exists(os.path.join(directory, newFilename)):
        newFilename = get_valid_filename(directory, filename, extention, index + 1)

    return newFilename


if __name__ == '__main__':

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pymediainfo'])
    from pymediainfo import MediaInfo
    directory = os.getcwd()
    files = os.listdir(directory)

    for filename in files:
        alreadyDone = filename[:8].isnumeric() and filename[8] == "_" and filename[9:15].isnumeric();
        if (filename.endswith('.MP4') or filename.endswith('.mp4')) and not alreadyDone:
            media_info = MediaInfo.parse(os.path.join(directory, filename))
            for track in media_info.tracks:
                if track.track_type == "Video":
                    date_of = str(track.encoded_date)
                    date_of = date_of.replace(':', '')
                    date_of = date_of.replace('UTC ', '')
                    date_of = date_of.replace('-', '')
                    date_of = date_of.replace(' ', '_')
                    # newFilename = get_  date_of + filename[-4:];

                    os.rename(filename, get_valid_filename(directory, date_of, filename[-4:], 0))




