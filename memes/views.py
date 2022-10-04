import random
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from .models import MemesModel
import sqlite3
import wget
import os.path


def view(request):
    response = ""
    status = 500
    number = ""
    while status != 200:
        number = str(random.randint(20000, 80000))
        response = requests.get("https://www.memify.ru/meme/" + number + "/kotik/")
        status = response.status_code
    soup = BeautifulSoup(response.text, "lxml")
    soup = str(soup.figure.img)
    soup = soup[soup.find('https'):]
    data = {"memes": soup[:-3]}
    #save parsing images I
    #                    I
    #                    V

    # if not os.path.exists('/Users/peeon/PycharmProjects/djangoProject3/media/' + number + '.jpg'):
    #     wget.download(soup[:-3], '/Users/peeon/PycharmProjects/djangoProject3/media/'+number+'.jpg')
    # locals()[number] = MemesModel
    # obj = MemesModel.objects.latest('id')
    # obj.download = '/Users/peeon/PycharmProjects/djangoProject3/media/'+number+'.jpg'
    # obj.save()
    return render(request, 'memesPage.html', context=data)


