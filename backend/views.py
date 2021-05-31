from django.shortcuts import render, redirect
from django.views import View
from backend.utils import generateUrl
from backend.models import ShortenedUrl
from django.http import HttpResponse
import requests


class CreateUrl(View):
    def get(self, request):
        if request.user.is_authenticated:
            current_user = request.user
            owner_urls = ShortenedUrl.objects.filter(owner=current_user)
            context = {
                "urls": owner_urls,

            }
            return render(request, "backend/index.html", context)
        return render(request, "backend/index.html")

    def post(self, request):
        originalUrl = request.POST.get('originalURL')
        title = request.POST.get('title')
        if not title:
            title = "Not Mentioned"
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

            if is_url == True:
                shortenedUrl = generateUrl()
                if request.user.is_authenticated:
                    owner = request.user
                    new_object = ShortenedUrl(originalUrl = originalUrl, shortenedUrl = shortenedUrl, title=title, owner=owner)
                else:
                    new_object = ShortenedUrl(originalUrl = originalUrl, shortenedUrl = shortenedUrl, title=title)
                new_object.save()
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
    
    
