from datetime import datetime
from django.shortcuts import render


def home(request):
    return render(request,"home.html",context={'data':{
        "name":"yeasin",
        "arr":[3,2,1],
        "number":25,
        "intro":"i'm Yeasin",
        "date":datetime.now(),
        "arrDict":[
                    {'name': 'zed', 'age': 19},
                    {'name': 'amy', 'age': 22},
                    {'name': 'joe', 'age': 31},
                ],
        "div":21,
        
    }})