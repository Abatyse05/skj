from django import forms
from .models import Player
from .models import Team
from .models import Ligue
from .models import PlayerHistory

class PlayerHistoryForm(forms.ModelForm):
    class Meta:
        model = PlayerHistory
        fields = ['player', 'team', 'start', 'end']
        widgets = {
            'start': forms.DateInput(attrs={'type': 'date'}),
            'end': forms.DateInput(attrs={'type': 'date'}),
        }

class LigueForm(forms.ModelForm):
    class Meta:
        model = Ligue
        fields = ['name', 'prize', 'season']



class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'category', 'ligue']



class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['nickname', 'name', 'surname', 'team', 'category']