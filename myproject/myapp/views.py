from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt       # 임시 POST 보안 우회
from django.shortcuts import redirect
import random

nextId = 4
topics = [
    {"id":1, "title":"Routing", "body":"Routing is .."},
    {"id":2, "title":"View", "body":"View is .."},
    {"id":3, "title":"Model", "body":"Model is .."}
]

# Create your views here.
def HTMLTemplate(articleTag):
    global topics    
    ol = ""
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f"""
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ol>
            {ol}
        </ol>
        {articleTag}
        <ul>
            <li><a href="/create/">create</a></li>
        </ul>
    </body>
    </html>
    """

def index(request):
    article = """    
    <h2>welcome</h2>
    Hello, Django    
    """
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    global topics
    article = ""
    for topic in topics:
        if topic["id"] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))


@csrf_exempt    # 임시 POST 보안 우회
def create(request):
    global nextId

    if request.method == "GET":
        article = """
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        """
        return HttpResponse(HTMLTemplate(article))
    elif request.method == "POST":
        title = request.POST["title"]
        body = request.POST["body"]
        newTopic = {"id":nextId, "title":title, "body":body}
        topics.append(newTopic)

        url = "/read/"+str(nextId)
        nextId += 1
        return redirect(url)