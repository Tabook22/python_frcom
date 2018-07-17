from django.http import HttpResponse

def home(request):
    return HttpResponse("الحمد لله رب العالمين")