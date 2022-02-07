from django.http import HttpResponse

frame = f"""
<html>
    <head lang="ko>
        <meta charset="utf-8">
        <meta name="author" content="Park Seonghun">
        <meta name="description" content="My Schedule && My Diary && My Story. Top Topic is Machine Learning, Deep Learning, Computer programming, Math, Statics, ...">
        <link rel="shortcut icon">
        <title>별로의 놀이터</title>
    </head>

    <body>
        <h1>Byeol_Lo's Play Ground</h1>
    </body>
</html>
"""

def index(request) :
    global frame
    return HttpResponse(frame)