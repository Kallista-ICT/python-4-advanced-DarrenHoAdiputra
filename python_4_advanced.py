player_art = r"""
      O  
     /|\
     / \
"""

idle_warrior_art = r"""
,/|\  
       //o=o\        
       \\ - //  
       (/ * \)    
   /|--(::::)--|\
  / |___\_/___| \  
   /    |||    \  
  /     |||     \  
 (      |||      )  
  \    |||||    /  
   \__/ ||| \__/  
       / | \ ⚔️=======  
      /  |  \  
     /   |   \  
    /    |    \  
   /     |     \  
  /      |      \  
 /       |       \  
/        |        \  
"""

attack_warrior_art = r"""


player_health = 100
player_attack_damage = 40
defense_multiplier = 0.5

warrior_name = "The Undefeated Warrior"
warrior_health = 150
warrior_attack_damage = 30
warrior_attack_damage = 40

warrior_mode = "idle"

while player_health > 0 and warrior_health > 0:
    if warrior_mode == "idle":
        print()
    elif warrior_mode == "attack":
        print()