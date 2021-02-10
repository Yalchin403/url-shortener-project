from django.shortcuts import render, redirect
from django.views import View
from backend.forms import TaskForm
from backend.utils import generateUrl
from backend.models import ShortenedUrl
from django.http import HttpResponse
import requests


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
            try:
                if originalUrl[0:4] != "http":
                    originalUrl = "http://" + originalUrl                
                requests.get(originalUrl, headers={
"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
})
                is_url = True

            except:
                print("There was an error with request.. sorry")
                is_url = False

            if is_url == True:
                try:
                    alreacy_have = ShortenedUrl.objects.get(originalUrl = originalUrl)
                    shortenedUrl = alreacy_have.shortenedUrl
                    return render(request, "backend/shortened.html", {"createdUrl": shortenedUrl})
                except:
                    shortenedUrl = generateUrl()
                    new_object = ShortenedUrl(originalUrl = originalUrl, shortenedUrl = shortenedUrl)
                    new_object.save()
                    createdUrl = "http://localhost:8000/" + shortenedUrl
                    return render(request, "backend/shortened.html", {"createdUrl": shortenedUrl})
            else:
                
                return HttpResponse("Hmmmm, cheating?")
        else:
            
            return HttpResponse("Form is not valid !")
        
        

        
        
class RedirectToOriginal(View):
    def get(self, request, shortenedUrl):
        try:
            obj = ShortenedUrl.objects.get(shortenedUrl = shortenedUrl)
            originalUrl = obj.originalUrl
            return redirect(originalUrl)
        except:
            return HttpResponse("You are trying to access non-exsisting url.. Please check the url that you entered.")
    
    
