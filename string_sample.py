#Les chaines de carateres
chaine="Bonjour tout le monde"
print '\nOriginal: ', chaine
print "\nFonction upper(): ", chaine.upper()
print "\nFonction lower(): ", chaine.lower()
#Operation sur les chaines de carateres
chaine1='Boujour'
chaine2='Lili'
print "Adition de deux chaines", chaine1+" "+chaine2
print "Multiplication de d'une chaines", chaine2*3
# Bonjour Lili
# BonjourLili

#sous-chaine (substring)
print "\n------",chaine,"------"
l=len(chaine)
print "Longueur d'une chaine avec fonction len(): ", l
print "Position de 0 a 3", chaine[0:3]
print "Position de 10 a len: ", chaine[10:l]
print "Position de 10 a len: ", chaine[10]

print "position -1: ", chaine  [-1]
