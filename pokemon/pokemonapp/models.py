from django.db import models

# Create your models here.

# 001 - To create a pokemon constructor class, I will give it a name, type, and level perameters. Its max health will be determined by its level. I will give it a default level of 5. Its starting health is its max health and it is not knocked out when it starts.
class Pokemon:
    def __init__(self, name, type, level = 5):
        self.name = name
        self.level = level
        self.health = level * 5
        self.max_health = level * 5
        self.type = type
        self.is_knocked_out = False

# 002 - I will use the __repr__ method to print a string of a created pokemon that interpolates its stats. 
    def __repr__(self):
        return "Level {level} {name} has {health} hit points remaining. It is a {type} type Pokemon".format(level = self.level, name = self.name, health=self.health, type = self.type)