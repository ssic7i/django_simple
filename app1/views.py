from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import json
from app1.models import Choice

# Create your views here.
def view1(request, *args, **kwargs):
    return HttpResponse("asdasd")

class SampleClassView(View):

    def post(self, request):
        return HttpResponse(request.read())

    def get(self, requset):
        all_results = Choice.objects.all()
        return HttpResponse(json.dumps(list(all_results.values())))

