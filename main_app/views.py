import requests
# from Serializer  import   TodoSerializer
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from main_app.models import TodoModel 
from django.http import HttpResponse
from django.http import HttpResponse
import datetime
from django.views.generic import TemplateView, ListView
from django.db.models import Q

def say_hello(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def get_data(request):

    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todos = response.json()
    count = len(todos)
    if count > 0 :
        TodoModel.objects.all().delete()
        for i in todos:
                myModel = TodoModel(
                    userId = i['userId'],
                    id = i['id'],
                    completed = i['completed'],
                    title = i['title'],
                    active = True
                )
                myModel.save()
        now = datetime.datetime.now()
        
        html = "<html><body>%s  Record Fetch At %s.</body></html>" %(count , now)
        return HttpResponse(html)
    else:
        html = "<html><body>No Data Fetched"
        return HttpResponse(html)

def home(request):
    # headers = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMjE0MzgzOGJhNTYxZmM0ODlhZjU3ZmE5M2NmZjc4NCIsInN1YiI6IjY1Zjg5YzYwOGVlMGE5MDE4NmNkMjgyYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.RAuwO5L1OcEGdspgXDKawso-X7ib8f-KVEKjuacYP_8"
    # url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
    # headers = {"accept": "application/json"}
    # response1 = requests.get(url, headers=headers)
    # print(response1)
    # api key : 32143838ba561fc489af57fa93cff784
    # API Read Access Token:
    # eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMjE0MzgzOGJhNTYxZmM0ODlhZjU3ZmE5M2NmZjc4NCIsInN1YiI6IjY1Zjg5YzYwOGVlMGE5MDE4NmNkMjgyYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.RAuwO5L1OcEGdspgXDKawso-X7ib8f-KVEKjuacYP_8
    # response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    # todos = response.json()
    condition =""
    try:
        condition = request.GET.get("condition")
    except:
        condition
    # request.GET['num1']
    print(condition)
    if condition=="":
        todos = TodoModel.objects.all()
    else:
        todos = TodoModel.objects.get(Q(title__startswith=condition) | Q(title__endswith=condition))
    todos = TodoModel.objects.all()
    # paging
    p = Paginator(todos, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    # sending the page object to index.html
    # print(page_obj)
    print(page_obj.object_list)
    return render(request, "main_app/phome.html", context)

    # paging
    # return render(request, "main_app/home.html", {"data": todos})
# def save_response_data(data):
#     # here validate...
#     json_data = {}
#     # I want the user instance that is making the request
#     serializer = TodoSerializer(data=json_data)

#     if serializer.is_valid():
#       serializer.save()

#     return json_data
