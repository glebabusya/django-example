from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    def get(self, request):
        template = 'Index.html'
        return render(request, template)