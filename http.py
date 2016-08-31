# -*- coding: utf-8 -*-
import os
import csv
import random
from flask import Flask,request, redirect
from flask import render_template
from werkzeug.utils import secure_filename

fileupstatus = None
filmList = {"Number":[], "Title":[], "Year":[], "Director":[], "Rating":[], "Tags":[], "URL":[]}
filmNumber = 0;
notestyle = "alert alert-info"

uploadfolder = 'c:\\users\\astahov\\PycharmProjects\\RandomMovie\\uploads'
uploadexs = set(['csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = uploadfolder

def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1] in uploadexs

def fileOpen(filename):
    global filmList, filmNumber
    file = open(filename, 'rb')
    filmListDR = csv.DictReader(file, delimiter=',')
    for row in filmListDR:
        filmList["Number"].append(filmNumber)
        filmList["Title"].append(str(row['Title']))
        filmList["Year"].append(str(row['Year']))
        filmList["Rating"].append(str(row['IMDb Rating']))
        filmList["Tags"].append(str(row['Genres']))
        filmList["Director"].append(str(row['Directors']))
        filmList["URL"].append(str(row['URL']))
        filmNumber += 1
    filmNumber -= 1
    file.close()

@app.route('/')
def index():
    global fileupstatus, notestyle
    return render_template("index.html",
                           title="RandomMovie",
                           fileupstatus=fileupstatus,
                           notestyle=notestyle)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global fileupstatus, uploadprogress, filmNumber, notestyle, filmList
    if request.method == 'POST':
        if request.form['submit'] == 'upload':
            if 'file' not in request.files:
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                fileupstatus = True
                fileOpen(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                filmNumberCheck = filmNumber % 10
                notestyle = "alert alert-success"
                return render_template("index.html",
                                       title="RandomMovie",
                                       fileupstatus=fileupstatus,
                                       filmNumber=filmNumber,
                                       filmNumberCheck=filmNumberCheck,
                                       notestyle=notestyle)
    filmNumber = 0

@app.route('/', methods=['GET', 'POST'])
def randomFilm():
    global filmList
    if request.method == 'GET':
        if request.form['submit'] == 'getRandom':
            randomFilmNumber = random.choice(filmList["Number"])
            randomFilmTitle = str(filmList["Title"][randomFilmNumber])
            randomFilmDirector = str(filmList["Director"][randomFilmNumber])
            randomFilmTags = str(filmList["Tags"][randomFilmNumber])
            randomFilmRating = str(filmList["Rating"][randomFilmNumber])
            randomFilmYear = str(filmList["Year"][randomFilmNumber])
            randomFilmURL = str(filmList["URL"][randomFilmNumber])
            return render_template("index.html",
                                   randomFilmTitle=randomFilmTitle,
                                   randomFilmDirector=randomFilmDirector,
                                   randomFilmTags=randomFilmTags,
                                   randomFilmRating=randomFilmRating,
                                   randomFilmYear=randomFilmYear,
                                   randomFilmURL=randomFilmURL)

app.run()