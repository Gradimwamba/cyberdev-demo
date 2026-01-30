# Voici notre premier project
# nous voulons un code python qui permet a l'utilisateur de deviner un nombre:
# Entrer un nombre, et quand l'utilisateur entre le nombre, ça dit si le nombre entré est grand ou petit. ou il a trouver le bon nombre


number = int(input("Entrer un nombre : ? "))

if number >= 100 :
    print("Le nombre entré est grand")
else :
    print("Le nombre entré est petit")

print("Vous avez trouvé le bon nombre !")