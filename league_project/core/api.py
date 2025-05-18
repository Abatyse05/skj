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



@router.get("/full")
def get_full_data(request):
    players = [
        {
            "id": p.id,
            "nickname": p.nickname,
            "name": p.name,
            "surname": p.surname,
            "team": p.team.name if p.team else None,
            "category": p.category.name if p.category else None,
        }
        for p in Player.objects.select_related("team", "category").all()
    ]

    teams = [
        {
            "id": t.id,
            "name": t.name,
            "ligue": t.ligue.name if t.ligue else None,
            "category": t.category.name if t.category else None,
        }
        for t in Team.objects.select_related("ligue", "category").all()
    ]

    ligues = list(Ligue.objects.values("id", "name", "prize", "season"))
    categories = list(Category.objects.values("id", "name"))

    history = [
        {
            "id": h.id,
            "player": h.player.nickname,
            "team": h.team.name,
            "start": h.start,
            "end": h.end,
        }
        for h in PlayerHistory.objects.select_related("player", "team").all()
    ]

    return {
        "players": players,
        "teams": teams,
        "ligues": ligues,
        "categories": categories,
        "history": history,
    }


