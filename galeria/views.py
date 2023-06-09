from django.shortcuts import render,get_object_or_404
from galeria.models import fotografia

def index(request):
    fotografias = fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    
    return render(request,'galeria/index.html',{"cards":fotografias})

def imagem(request,foto_id):
    Fotografia = get_object_or_404(fotografia,pk=foto_id)
    return render(request,'galeria/imagem.html',{"Fotografia":Fotografia}) 
