from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req, 'home.html')

def playlist(req):
    playlist = [
        'Tera Yaar Hoon Main',
        'Te amo',
        'Tera Naam',
        'Naatu Naatu',
        'Rooba Rooba'
                ]
    return render(req, 'playlist.html', {'playlist': playlist})

def controls(req,song):
    return render(req, 'musicControls.html', {'song':song})