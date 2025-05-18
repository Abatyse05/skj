from django.db import models

class Ligue(models.Model):
    name = models.CharField(max_length=100)
    prize = models.DecimalField(max_digits=10, decimal_places=2)
    season = models.CharField(max_length=20)


    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ligue = models.ForeignKey(Ligue, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"

class Player(models.Model):
    nickname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nickname} ({self.name} {self.surname})"

class PlayerHistory(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)

class PriceList(models.Model):
    position = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ligue = models.ForeignKey(Ligue, on_delete=models.CASCADE)
