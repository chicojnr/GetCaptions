from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import gc
import json

app = Flask(__name__)

request_counter = 0  # Contador de requisições

@app.after_request
def cleanup(response):
    global request_counter

    # Incrementa o contador de requisições
    request_counter += 1

    # Limpa a memória a cada 5 requisições
    if request_counter % 5 == 0:
        gc.collect()

    return response

@app.route('/')
def index():
        try:
                srt = YouTubeTranscriptApi.get_transcript(request.args.get('id'), languages=['pt'])
                caption_ret = []
                for i in srt:
                        caption_ret.append(i)

                return jsonify(caption_ret)
        except Exception as e:
                return json.dumps({"error": str(e)}, ensure_ascii=False)

if __name__ == '__main__':
    app.run()


# from flask import Flask
# from flask import request
# from youtube_transcript_api import YouTubeTranscriptApi
# import json

# app = Flask(__name__)

# @app.get('/')
# def index():
#         srt = YouTubeTranscriptApi.get_transcript(request.args.get('id'), languages=['pt'])
#         #with open("subtitles.txt", "w") as f:
#         caption_ret = []
#         # iterating through each element of list srt
#         for i in srt:
#                 # writing each element of srt on a new line
#                 #f.write("{}\n".format(i))
#                 caption_ret.append(i)

#         return json.dumps(caption_ret, ensure_ascii=False)

# if __name__ == '__main__':
#         app.run()