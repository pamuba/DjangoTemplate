from django.shortcuts import render

def exmaple_view(request):
    #localhost:8000/my_app/example.html
    return render(request, 'my_app/example.html')