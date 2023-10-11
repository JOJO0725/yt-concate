import yt_dlp

from .step import Step
import time


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        ydl_opts = {
            'writesubtitles': True,
            'writeautomaticsub': True,
            'skip_download': True,
            'subtitleslangs': ['en'],
            }
        for url in data:
            print('downloading caption for', url)
            if utils.caption_file_exists(url):
                print('found existing!')
                continue

            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    en_caption_convert_to_srt = str(ydl.download([url]))

            except (KeyError,AttributeError):
                print('Error when downloading for', url)
                continue
            text_file = open(utils.get_caption_filepath(url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print('took', end - start, 'seconds')
