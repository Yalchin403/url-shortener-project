from django.shortcuts import render, redirect
from django.views import View
from backend.utils import generateUrl
from backend.models import ShortenedUrl
from django.http import HttpResponse
import requests
from django.contrib import messages
from django.shortcuts import get_object_or_404


class CreateUrl(View):
    def get(self, request):
        if request.user.is_authenticated:
            current_user = request.user
            owner_urls = ShortenedUrl.objects.filter(owner=current_user).order_by('-createdTime')
            context = {
                "urls": owner_urls,

            }
            return render(request, "backend/index.html", context)
        return render(request, "backend/index.html")

    def post(self, request):
        originalUrl = request.POST.get('originalURL')
        copy_of_url = originalUrl

        title = request.POST.get('title')
        if not title:
            title = "Not Mentioned"

        if originalUrl == "":
            messages.error(request, 'You cannot submit empty URL...')
            return redirect("backend:generate-url")

        else:
            try:
                if originalUrl[0:4] != "http":
                    originalUrl = "http://" + originalUrl                
                requests.get(originalUrl, headers={
"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
})
                is_url = True

            except:
                messages.error(request, f'{copy_of_url}, is not valid URL...')
                return redirect("backend:generate-url")

            if is_url == True:
                if len(copy_of_url) <= 26:
                    messages.error(request, f'{copy_of_url}, is already short...')
                    return redirect("backend:generate-url")
                shortenedUrl = generateUrl()
                if request.user.is_authenticated:
                    owner = request.user
                    new_object = ShortenedUrl(originalUrl = originalUrl, shortenedUrl = shortenedUrl, title=title, owner=owner)
                else:
                    new_object = ShortenedUrl(originalUrl = originalUrl, shortenedUrl = shortenedUrl, title=title)
                new_object.save()
                return render(request, "backend/shortened.html", {"createdUrl": shortenedUrl})
        

class RedirectToOriginal(View):
    def get(self, request, shortenedUrl):
        try:
            obj = ShortenedUrl.objects.get(shortenedUrl = shortenedUrl)
            originalUrl = obj.originalUrl
            return redirect(originalUrl)
        except:
            return redirect('https://http.cat/404')
            
    def post(self, request, shortenedUrl):
        return redirect('https://http.cat/405')

class DeleteUrl(View):
    def get(self, request, pk):
        return redirect('https://http.cat/405')
    
    def post(self, request, pk):
        url_obj = get_object_or_404(ShortenedUrl, pk=pk)
        if url_obj.owner != request.user:
            return redirect('https://http.cat/403')
        url_obj.delete()
        return redirect('backend:generate-url')
    
    
