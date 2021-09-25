from django.shortcuts import render, redirect
from django.views import View
from paste_zone.utils import generateSlug
from paste_zone.models import PasteZone
from django.http import HttpResponse
import requests
from django.contrib import messages
from django.shortcuts import get_object_or_404


class CreatePaste(View):
    def get(self, request):
        if request.user.is_authenticated:
            current_user = request.user
            owner_pastes = PasteZone.objects.filter(owner=current_user).order_by('-createdTime')
            context = {
                "pastes": owner_pastes,
            }

            return render(request, "paste_zone/paste_zone.html", context)
        return render(request, "paste_zone/paste_zone.html")

    def post(self, request):
        content = request.POST.get('pasteContent')
        title = request.POST.get('title')
        slug = generateSlug()
        owner = None

        if not title:
            title = "Not Mentioned"
        if request.user.is_authenticated:
            owner = request.user

        if owner:
            paste_zone_obj = PasteZone(slug=slug, content=content, owner=owner, title=title)

        else:
            paste_zone_obj = PasteZone(slug=slug, content=content, title=title)

        paste_zone_obj.save()
        return render(request, "paste_zone/pasted.html", {"pasted_slug": slug})


class DetailView(View):

    def get(self, request, slug):
        paste_obj = PasteZone.objects.get(slug = slug)
        context = {
            "paste": paste_obj
        }
        return render(request, "paste_zone/detail_view.html", context)


class DeletePaste(View):
    def get(self, request, pk):
        return redirect('https://http.cat/405')

    def post(self, request, pk):
        paste_obj = get_object_or_404(PasteZone, pk=pk)
        if paste_obj.owner != request.user:
            return redirect('https://http.cat/403')
        paste_obj.delete()
        return redirect('paste_zone:generate-paste')
