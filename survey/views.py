from django.http import HttpResponse

frame = """
<!DOCTYPE html>
<html>
    <head lang="ko">{head}</head>
    <body>
        {view}
    </body>
</html>
"""

head = f"""
        <meta charset="utf-8">
        <meta name="author" content="Park Seonghun">
        <meta name="description" content="My Schedule && My Diary && My Story. Top Topic is Machine Learning, Deep Learning, Computer programming, Math, Statics, ...">
        <link rel="shortcut icon" href="/static/fabicon.ico">
        <link rel="icon" href="/static/fabicon.ico">
        <title>별로의 놀이터</title>
"""

views = {
    "main" : f"""<h1> 안녕! 난 채뽓이야! :)</h1>
        <h2>나랑 대화하자!</h2>
        <form>
            <p><textarea id="usr_chat"placeholder="봇이랑 채팅하기"></textarea></p>
            <p><input type="submit" value="전송"/></p>
        </form>
        """
}


def index(request) :
    
    global frame, head, views

    return HttpResponse(frame.format(head=head, view=views["main"]))
