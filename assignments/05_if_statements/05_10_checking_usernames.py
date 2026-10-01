''''''
# Ciani Mason
current_users = ['admin', 'deathbringer225', 'csacademy225', 'pretty_cicic225', 'UnderDaC221']

new_users = ['admin', 'MangoQueen', 'deathbringer225', 'AnimeGirl', 'Cici225']

current_users_lower = []

for username in current_users:
    current_users_lower.append(username.lower())

for new_username in new_users: 
    if new_username.lower()  in current_users_lower: 

     print("That username is already taken. You will need to enter a new username.")
else: 
   print('That username is available."')
