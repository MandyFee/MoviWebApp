#!/usr/env python3
"""
Console Adventure Game - A text-based RPG adventure
Navigate through dungeons, fight monsters, and collect treasures!
"""

import random
import time
import sys
from posixpath import expanduser
from typing import Dict, List, Optional

class Player:
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.level = 1
        self.experience = 0
        self.gold = 50
        self.inventory = ["Health Potion", "Iron Sword"]
        self.attack_power = 15
        self.defense = 5
        self.location = "village"

    def level_up(self):
        """Increase player level and stats"""
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        self.attack_power += 5
        self.defense += 2
        print(f"\n LEVEL UP! You are now level{self.level}!")
        print(f"Health: {self.health}/{self.max}")
        print(f"Attack: {self.attack_power}, Defense: {self.defense}")

    def take_damage(self, damage: int):
        """Reduce player health"""
        actual_damage = max(1, damage - self.defense)
        self.health = max(0, self.health - actual_damege)
        return actual_damage

    def heal(self, amout: int):
        """Add experience and check for level up"""
        self.exerience += exp
        exp_needed = self.level * 100
        if self.experience >= exp_needed:
            self.experience -= exp_needed
            self.level_up()

    def is_alive(self) -> bool:
        """Check if player is alive"""
        return self.health > 0

class Monster:
    def __init__(self, name: str, health: int, attack: int, defense: int, gold_reward: int):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack
        self.defense = defense
        self.gold_reward = gold_reward
        self.exp_reward = exp_reward

    def take_damage(self, damage: int):
        """Reduce monster health"""
        actual_damage = max(1, damage - self.defense)
        self.health = max(0, self.health - actual_damage)
        return actual_damage

    def is_alive(self) -> bool:
        """Check if monster is alive"""
        return self.health > 0

class Game:
    def __init__(self):
        self.play = None
        self.game_running = True
        self.current_monster = None
        self.locations = {
            "village": {
                "description": "A peaceful village with shops and inns",
                "actions": ["shop", "inn", "dungeon", "status", "inventory"]
            },
            "dungeon": {
                "description": "A dark and dangerous dungeon filled with monsters",
                "actions": ["explore", "rest", "village", "status", "inventory"]
            },
            "shop": {
                "description": "A merchant´s shop with weapons and potions",
                "actions": ["buy", "sell", "village", "status", "inventory"]
            },
            "inn": {
                "description": "A cozy in where you can rest and heal",
                "actions": ["rest", "village", "status", "inventory"]
            }
        }

    def print_header(self):
        """Print game header"""
        print("=" * 60)
        print("  CONSOLE ADVENTURE GAME  ")
        print("=" * 60)

    def print_separator(self):
        """Get separator line"""
        print("-" * 40)

    def get_player_name(self):
        """Get player name from user input"""
        whit T