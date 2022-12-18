import os
import subprocess
import sys

if __name__ == '__main__':
    # вот пример комментария
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pymediainfo'])
    from pymediainfo import MediaInfo
    directory = os.getcwd()
    files = os.listdir(directory)

    for filename in files:
        if filename.endswith('.MP4') and filename.startswith('GH'):
            media_info = MediaInfo.parse(os.path.join(directory, filename))
            for track in media_info.tracks:
                if track.track_type == "Video":
                    date_of = str(track.encoded_date)
                    date_of = date_of.replace(':', '')
                    date_of = date_of.replace('UTC ', '')
                    date_of = date_of.replace('-', '')
                    date_of = date_of.replace(' ', '_')

            os.rename(filename, date_of + filename[8:])




