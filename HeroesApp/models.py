from django.db import models

# Create your models here.


class SuperHero(models.Model):
    real_name = models.CharField(max_length=45)
    hero_name = models.CharField(max_length=45)
    age = models.IntegerField()
    # teams_on = models.ManyToManyField(SuperTeam, related_name="heroes_on_team")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.hero_name} is actually {self.real_name}"


class SuperTeam(models.Model):
    team_name = models.CharField(max_length=45)
    from_where = models.CharField(max_length=45)
    heroes_on_team = models.ManyToManyField(SuperHero, related_name="teams_on")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.team_name}"
