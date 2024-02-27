from django.shortcuts import render, HttpResponse
from polls.models import slideshow, tablecell,product_image,comments


# Create your views here.

def home(request):
    slide = slideshow.objects.raw("SELECT * FROM polls_slideshow")
    tablecel = tablecell.objects.raw("SELECT * FROM polls_tablecell")
    image = product_image.objects.raw("SELECT * FROM polls_product_image")
    coment = product_image.objects.raw("SELECT * FROM polls_comments")
    return render(request, "index.html", {'slide':slide,'tablecel':tablecel,'image':image,'coment':coment})



def endirimurl(request,id):
    if id !=None:
        image = product_image.objects.raw("SELECT * FROM polls_product_image WHERE id = '%s' "% (id) )
        image2 = product_image.objects.raw("SELECT * FROM polls_product_image ")
        return render(request, 'endirim.html', {'image':image,'image2':image2})


    else:
        image2 = product_image.objects.raw("SELECT * FROM polls_product_image ")
        image = product_image.objects.raw("SELECT * FROM polls_product_image WHERE id = 1 " )
        return render(request, 'endirim.html', {'image':image,'image2':image2})


def etrafli(request):
    return render(request, 'etrafli.html', {})


def guller(request):
    return render(request, 'guller.html', {})


def blogumuz(request):
    return render(request, 'blogumuz.html', {})


def haqqimizda(request):
    return render(request, 'haqqimizda.html', {})


def elaqe(request):
    return render(request, 'elaqe.html', {})