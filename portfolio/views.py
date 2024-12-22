import os
from django.conf import settings
from django.shortcuts import render

def index(request):
    return render(request, 'portfolio/index.html')

def portfolio(request):
    # Ruta absoluta a la carpeta de imágenes
    image_folder = os.path.join(settings.BASE_DIR, 'static/images/')
    
    print("Ruta a la carpeta de imágenes:", image_folder)  # Imprime la ruta completa

    # Generar lista de imágenes
    images = []
    for filename in os.listdir(image_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            images.append({
                "thumbnail_url": f"/static/images/{filename}",
                "full_url": f"/static/images/{filename}",
                "title": os.path.splitext(filename)[0].replace('_', ' ').capitalize()
            })
    
    return render(request, 'portfolio/index.html', {"images": images})

