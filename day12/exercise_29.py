#Namespaces:
#Local vs Global Scope

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f'enemies inside function: {enemies}')

# increase_enemies()
# print(f'enemies outside function: {enemies}')

# # Local Scope

# def drink_potion():
#     potion_streng = 2
#     print(potion_streng)

# drink_potion()

# print(potion_Streng)

#Global Scope
# player_health = 10

# def game():
#     def drink_potion():
#         potion_streng = 2
#         print(player_health)
#     drink_potion()

# print(player_health)

# There is no Block Scope

# game_level = 3
# def create_enemy():
#     enemies = ['Skeleton', 'Zombie', 'Alien']
#     if game_level < 5:
#         new_enemy = enemies[0]
#     print(new_enemy)

# How to Modify Variables with Global Scope

# enemies = 1

# def increase_enemies():
#     print(f'enemies inside function: {enemies}')
#     return enemies + 1

    
# increase_enemies()
# print(f'enemies outside function: {enemies}')

# Python Constants & Global Scope

PI = 3.14159
URL = 'https://www.google.com'
TWITTER_HANDLE = '@Lifimastar'

