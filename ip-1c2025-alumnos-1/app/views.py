# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from app.layers.utilities.card import Card



#
def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados: uno de las imágenes de la API y otro de favoritos, ambos en formato Card, y los dibuja en el template 'home.html'.
def home(request):
    
    images=services.getAllImages()#llamamos a la funcion de services(getAllImages) que nos devuleve una lista con las cards de los pokemon.
    favourite_list=services.getAllFavourites(request)#llamamos a la funcion de services(getAllFavourites) que nos devuleve una lista con las cards de los pokemon favoritos del usuario logueado.
    return render(request, 'home.html', { 'images': images ,'favourite_list':favourite_list  })#


# función utilizada en el buscador.
def search(request):#
    name = request.POST.get('query', '')
    name_card=services.filterByCharacter(name)
    # si el usuario ingresó algo en el buscador, se deben filtrar las imágenes por dicho ingreso.
    if (name_card!=[]) :
        images = name_card
        favourite_list = []
        


        return render(request, 'home.html', { 'images':images, "favourite_list":favourite_list })
    else:
        return redirect("home")

# función utilizada para filtrar por el tipo del Pokemon
def filter_by_type(request):
    type = request.POST.get('type', '')
    type_card=services.filterByType(type)

    if type_card != []:
        images = type_card # debe traer un listado filtrado de imágenes, segun si es o contiene ese tipo.
        favourite_list = []

        return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })
    else:
        return redirect('home')

# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    favourite_list=services.getAllFavourites(request)
    return render(request,"favourites.html",{'favourite_list': favourite_list })
    

@login_required
def saveFavourite(request):
    guardar=services.saveFavourite(request)  # Guarda el favorito
    # Después de guardar, redirige a home.html
    return redirect('home')

    return render
@login_required
def deleteFavourite(request):
    borrar_list=services.deleteFavourite(request)
    favourite_list = services.getAllFavourites(request)
    return render(request, 'favourites.html', { 'favourite_list': favourite_list,  'borrar_list': borrar_list })
    

@login_required
def exit(request):
    logout(request)
    return redirect('home')
