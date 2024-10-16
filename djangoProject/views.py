from django.shortcuts import render
from django.views import View


class HelloWorld(View):
    def get(self, request):
        return render(request, "hello.html", {"name": "Ayesha"})
