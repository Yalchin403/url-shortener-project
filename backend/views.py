from django.shortcuts import render, redirect
from django.views import View
from backend.utils import generateUrl
from backend.models import ShortenedUrl
from django.http import HttpResponse
import requests


class CreateUrl(View):
    def get(self, request):
        return render(request, "backend/index.html")

    def post(self, request):
        originalUrl = request.POST.get('originalURL')
        title = request.POST.get('title')
        if originalUrl != None:
            try:
                if originalUrl[0:4] != "http":
                    originalUrl = "http://" + originalUrl                
                requests.get(originalUrl, headers={
"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
})
                is_url = True

            except:
                return render(request, "backend/error.html")
                is_url = False
            # line 21-28 can probably be replaced with: if requests.get(originalUrl).status_code == 200: is_url = true, else false 

            if is_url == True:
                try:
                    alreacy_have = ShortenedUrl.objects.get(originalUrl = originalUrl)
                    shortenedUrl = alreacy_have.shortenedUrl
                    return render(request, "backend/shortened.html", {"createdUrl": shortenedUrl})
                except:
                    shortenedUrl = generateUrl()
                    new_object = ShortenedUrl(originalUrl = originalUrl, shortenedUrl = shortenedUrl, title=title)
                    new_object.save()
                    createdUrl = "http://localhost:8000/" + shortenedUrl
                    return render(request, "backend/shortened.html", {"createdUrl": shortenedUrl})
            else:
                
                return render(request, "backend/error.html")
        else:
            
            return render(request, "backend/error.html")
        
        

        
        
class RedirectToOriginal(View):
    def get(self, request, shortenedUrl):
        try:
            obj = ShortenedUrl.objects.get(shortenedUrl = shortenedUrl)
            originalUrl = obj.originalUrl
            return redirect(originalUrl)
        except:
            return render(request, "backend/error.html")
    
    
