from django.shortcuts import render
from django.http import HttpResponse
from .models import *



def Index_home(request):
    category  =  Category.objects.all()
    author = Author.objects.all()

    ctx = {
        "cats":category,
        "auth":author
    }
    return render(request, 'home.html', ctx)



# def second_page(request):
#     html = "<h3> this is Burhon's  </h3>"
#     html += """
#        <br></br>
#        <ul>
#        <li><a href="http://127.0.0.1:8000/">Index  page</a></li>
#        <li><a href="http://127.0.0.1:8000/web2/">book genre</a> drama</li>
#        <li><a href="http://127.0.0.1:8000/web1/">book page</a><li>
#        </ul>
#        """
#     return HttpResponse(html)
#
#
# def third_page(request):        ##### joy tashlab beradi <br>
#     html="<h2>this is third page </h2>"
#     html +="""
#     <br></br>
#     <ul>
#     <li> <a href="http://127.0.0.1:8000/">Index page </a><li>
#     <li> <a href="http://127.0.0.1:8000/web1/home/">home  page</a> About home <li>
#     <li> <a href="http://127.0.0.1:8000/web2/">Book genre</a><li>
#     </ul>
#     """
#     return HttpResponse(html)
#
#


