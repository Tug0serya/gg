class character():
    def __init__(self, max_health, attack, armor):
        self.health = max_health
        self.attack = attack
        self.armor = armor
        self.current_health = max_health
    def attack(self, target):
        target.current_health -= self.attack * ((100 - target.armor) / 100)
        print(target.current_health, self.current_health)
    def get_current_state(self):
        state = f"Зоровье: {self.current_health}/{self.health} aтака: {self.attack}"
        return state

class player(character):
    def __init__(self, max_health, attack, armor):
        super().__init__(max_health, attack, armor)

class enemy(character):
    def __init__(self, max_health, attack, armor):
        super().__init__(max_health, attack, armor)

main_character = player(15, 5, 10)
goblin = enemy(5, 2, 0)
print(main_character.get_current_state())
main_character.attack(goblin)