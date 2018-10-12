#Problème 16
def solve_16(n):
    x = 2**n
    somme = 0
    while x != 0:
        somme += x%10 #ajout du chiffre le plus à droite
        x = x//10 #qu'on "retire" ensuite
    return somme

assert(solve_16(15) == 26)
print(solve_16(1000))


#Problème 22
def sum_name_score(nom):
    alphabet = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
    n = len(nom)
    somme = 0
    for i in range(n):
        l = nom[i]
        if l in alphabet: #pour ne pas compter les ' " ' car les chaînes de caractères des noms sont de la forme ' "NOM" '
            somme += ord(l) - 64 #pour bien ajouter le nombre correspondant à la position de la lettre dans l'alphabet
    return somme
    
def solve_22():
    f = open("p022_names.txt", 'r')
    for ligne in f:
        l = ligne
    f.close()
    liste_noms = l.split(',') #on range tous les noms du fichier dans une liste
    liste_noms_triee = sorted(liste_noms) #on trie cette liste
    score = 0
    n = len(liste_noms_triee)
    for i in range(1, n+1):
        score += i * sum_name_score(liste_noms_triee[i-1]) #pour chaque nom on fait le produit de sa position dans la liste triée avec la "somme de ses lettres"
    return score

assert(sum_name_score(' "COLIN" ') == 53)
print(solve_22())


#Problème 55
def renverser(x):
    rev=0
    while x != 0:
        rev = rev*10 + x%10
        x = x//10
    return rev

def solve_55(n):
    nb_lychrel = 0
    for i in range(n):
        j = 1
        y = i + renverser(i)
        while j < 50 and y != renverser(y): #à droite du and, on teste su y est un palindrome
            j += 1
            y += renverser(y)
        if j == 50: #i est alors, sous nos hypothèse, un nombre de Lychrel (nombre d'itérations nécesssaires => 50) 
            nb_lychrel += 1
    return nb_lychrel
            
print(solve_55(10000))
