with open ("/home/alex/Github/python-projects/dico_france.txt", "r", encoding="ISO-8859-1") as f:
    dico = f.read().split()
    import random
    chosen_word = (random.choice(dico))
    chosen_word = chosen_word.replace("é", "e").replace("è", "e").replace("ê","e").replace("î", "i").replace("â", "a").replace("ô", "o").replace("û", "u").replace("ë", "e").replace("ï", "i")
    chosen_word = chosen_word.upper()

crypted_word = ''
for i in range(len(chosen_word)):
        crypted_word += '-'

history = []
remlife = 0

level = input("Bonjour, à quel niveau souhaites-tu jouer? facile, moyen ou expert?\n")

if level == "facile":
    remlife = 10
elif level == "moyen":
    remlife = 7
elif level == "expert":
    remlife = 4

while level != "facile" and level != "moyen" and level != "expert":
        print("choix invalide")
        level = input("A quel niveau souhaites-tu jouer? facile, moyen ou expert?\n")
        if level == "facile":
            remlife = 10
        elif level == "moyen":
            remlife = 7
        elif level == "expert":
            remlife = 4


print("\n"+"Nombre de vies restantes: ",remlife,"\n")
print("longueur du mot:",len(chosen_word),"\n")
print(crypted_word, "\n")

while remlife >= 0:
    if remlife == 0:
        print("Perdu ! Le mot à trouver était "+chosen_word)
        break
    elif crypted_word == chosen_word:
        print("Gagné !")
        break  
    else:
        letter = input("Quelle lettre proposes-tu? ")
        while len(letter) > 1:
            print("Une lettre à la fois !")
            letter = input("Quelle lettre proposes-tu? ")
        letter = letter.upper()
        if letter in chosen_word:
            for i in range(len(chosen_word)):
                if letter == chosen_word[i]:
                    crypted_word = crypted_word[:i] + letter + crypted_word[i+1:] #https://favtutor.com/blogs/replace-character-string-python
            print("\n"+"Nombre de vies restantes: ",remlife,"\n")
            history.append(letter)
            if level != "expert":
                print("Lettres proposées:",history,"\n")
            print(crypted_word, "\n")
            
        else:
            remlife = remlife -1
            print("\n"+"Mauvais choix ! Essaies encore")
            print("\n"+"Nombre de vies restantes: ",remlife,"\n")
            history.append(letter)
            if level != "expert":
                print("Lettres proposées:",history,"\n")
            print(crypted_word, "\n")