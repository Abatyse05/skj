from ninja import Router
from core.models import Player
from typing import List
from pydantic import BaseModel
from core.models import Team
from core.models import Ligue
from core.models import Category
from core.models import PlayerHistory
from typing import Optional


router = Router()

class PlayerOut(BaseModel):
    id: int
    nickname: str
    name: str
    surname: str

@router.get("/players", response=List[PlayerOut])
def list_players(request):
    return Player.objects.all()

class TeamOut(BaseModel):
    id: int
    name: str

@router.get("/teams", response=List[TeamOut])
def list_teams(request):
    return Team.objects.all()


class LigueOut(BaseModel):
    id: int
    name: str
    prize: float
    season: str

@router.get("/ligues", response=List[LigueOut])
def list_ligues(request):
    return Ligue.objects.all()


class CategoryOut(BaseModel):
    id: int
    name: str

@router.get("/categories", response=List[CategoryOut])
def list_categories(request):
    return Category.objects.all()


class PlayerHistoryOut(BaseModel):
    id: int
    player: int
    team: int
    start: str
    end: Optional[str]

@router.get("/history", response=List[PlayerHistoryOut])
def list_player_history(request):
    return PlayerHistory.objects.all()



