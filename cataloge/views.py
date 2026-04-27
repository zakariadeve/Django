
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from .forms import FilmForm
from django.contrib.admin.views.decorators import staff_member_required

films_data = [
        {
            'titre': 'Batman',
            'annee': 2022,
            'note': 4.5,
            'description': "Une aventure sombre à Gotham avec action, mystère et héros masqué."
        },
        {
            'titre': 'Avatar',
            'annee': 2009,
            'note': 3.8,
            'description': "Un voyage visuel sur Pandora avec une histoire d'amour et d'émotions fortes."
        },
        {
            'titre': 'Inception',
            'annee': 2010,
            'note': 4.8,
            'description': "Un thriller psychologique qui explore les rêves et la réalité."
        },
    ]

def index(request):
    return render(request, 'index.html', {
        'top_films': films_data
    })


'''def index(request):
    return HttpResponse("<h1>Bienvenue dans la Médiathèque CineMagic</h1>")'''

def infos(request):
    return HttpResponse("CineMagic est une plateforme de gestion de films.")

# Nouvelle vue pour le routage dynamique
def film_detail(request, titre):
    film = next((item for item in films_data if item['titre'].lower() == titre.lower()), None)
    message_special = ""
    if titre == "Inception":
        message_special = "C'est notre film le plus populaire !"

    return render(request, 'film_detail.html', {
        'titre': titre,
        'film': film,
        'message_special': message_special
    })

def stats(request):
    return render(request, 'stats.html', {
        'films_data': films_data
    })
def contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'contact.html', {
                'form': ContactForm(),
                'success': True
            })

    return render(request, 'contact.html', {'form': form})
@staff_member_required
def ajouter_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.clean_annee_sortie()
            
            form.save()
            return redirect('index')
    else:
        form = FilmForm()

    return render(request, 'ajouter_film.html', {'form': form})



# Create your views here.
