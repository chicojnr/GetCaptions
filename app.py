from flask import Flask
from youtube_transcript_api import YouTubeTranscriptApi
import json

app = Flask(__name__)

@app.get('/')
def index():
        srt = YouTubeTranscriptApi.get_transcript('7le4AGwtH94', languages=['pt'])
        #with open("subtitles.txt", "w") as f:
        caption_ret = []
        # iterating through each element of list srt
        for i in srt:
                # writing each element of srt on a new line
                #f.write("{}\n".format(i))
                caption_ret.append(i)

        return json.dumps(caption_ret, ensure_ascii=False)

if __name__ == '__main__':
        app.run()