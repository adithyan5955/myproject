from django.shortcuts import render
from.models import Place,Teams
# Create your views here.
def index(request):
    objects = Place.objects.all()
    team = Teams.objects.all()
    return render(request,"index.html",{'objects':objects,'team':team})