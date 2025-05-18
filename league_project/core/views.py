from django.shortcuts import render
from .models import Team
from .forms import PlayerForm
from .models import Player
from .models import Ligue
from .models import *
from .forms import TeamForm
from .forms import LigueForm
from .forms import PlayerHistoryForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

def home(request):
    return render(request, 'core/home.html')


def add_player_history(request):
    if request.method == 'POST':
        form = PlayerHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_history_list')
    else:
        form = PlayerHistoryForm()
    
    return render(request, 'core/add_player_history.html', {'form': form})

def ligue_detail(request, ligue_id):
    ligue = get_object_or_404(Ligue, pk=ligue_id)
    teams = ligue.team_set.all()
    return render(request, 'core/ligue_detail.html', {
        'ligue': ligue,
        'teams': teams,
    })


def player_history_list(request):
    history = PlayerHistory.objects.select_related('player', 'team').all()
    return render(request, 'core/player_history_list.html', {'history': history})


def ligue_list(request):
    ligues = Ligue.objects.all()
    return render(request, 'core/ligue_list.html', {'ligues': ligues})


def edit_team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)

    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm(instance=team)

    return render(request, 'core/edit_team.html', {'form': form})


def team_detail(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    players = team.player_set.all()
    return render(request, 'core/team_detail.html', {
        'team': team,
        'players': players,
    })

def edit_player(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm(instance=player)
    
    return render(request, 'core/edit_player.html', {'form': form})



def add_ligue(request):
    if request.method == 'POST':
        form = LigueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # nebo 'team_list'
    else:
        form = LigueForm()
    
    return render(request, 'core/add_ligue.html', {'form': form})


def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm()
    
    return render(request, 'core/add_team.html', {'form': form})

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'core/team_list.html', {'teams': teams})


def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PlayerForm()
    
    return render(request, 'core/add_player.html', {'form': form})

def player_list(request):
    players = Player.objects.all()
    return render(request, 'core/player_list.html', {'players': players})


def player_detail(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    return render(request, 'core/player_detail.html', {'player': player})