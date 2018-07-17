from django.shortcuts import render

# Create your views here.

def add_view(request):
    return render(request, 'pages/add.html')
