from django.shortcuts import render, redirect
from django.views import View
from backend.forms import TaskForm
from backend.utils import generateUrl
from backend.models import ShortenedUrl
from django.http import HttpResponse


# Create your views here.
class CreateUrl(View):
    def get(self, request):
        form = TaskForm()
        content = {"form": form}
        return render(request, "backend/index.html", content)
    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            originalUrl = form.cleaned_data.get('originalUrl')
            if originalUrl[0:4] == "http":
                
                shortenedUrl = generateUrl()
                newUrl = ShortenedUrl(originalUrl = originalUrl, shortenedUrl = shortenedUrl)
                newUrl.save()
                return HttpResponse("I'm good")
            else:
                
                return HttpResponse("I'm good too")
        else:
            
            return HttpResponse("I'm good too")
        
class RedirectToOriginal(View):
    def get(self, request, shortenedUrl):
        try:
            qs = ShortenedUrl.objects.filter(shortenedUrl = shortenedUrl)
            obj = qs[0]
            originalUrl = obj.originalUrl
            return redirect(originalUrl)
        except:
            return HttpResponse("You are trying to access non-exsisting url.. Please check the url that you entered.")
    
    
