# 
import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# url = input("Ingresa la URL")
# print(url)
# # YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
from pytubefix import YouTube
from pytubefix.cli import on_progress
from flask import Flask, render_template, request, send_file
ssl._create_default_https_context = ssl._create_unverified_context
app = Flask(__name__, static_folder="static", static_url_path="")
def youtube_action(url, categoria):
    data= {}
    result = YouTube(url, on_progress_callback = on_progress)
    if categoria == 1:
        print(result.streams.get_highest_resolution().get_file_path())
        data=  {"title": result.title, "img": result.thumbnail_url, "video": result.streams.get_highest_resolution().url}
    elif categoria == 2:
        data=  {"title": result.title, "img": result.thumbnail_url, "video": result.streams.get_lowest_resolution().url}
    elif categoria == 3:
        data=  {"title": result.title, "img": result.thumbnail_url, "video": result.streams.get_audio_only().url}
    return data
@app.get("/")
def index():
    return render_template("index.html")
@app.post("/")
def test():
    print(request.json['username'], request.json['type'])
    result = youtube_action(request.json['username'], request.json['type'])
    return {"data": result}


