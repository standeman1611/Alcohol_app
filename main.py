Glazen = int(input("Hoeveel glazen heb je gehad?\n"))
Massa = float(input("Wat is je gewicht?\n"))
Tijd = float(input("Hoelang geleden was je laatste glas alcohol? (in uren)\n"))
Gender = input("Wat is je geslacht?\n")
Vocht = 0

if Gender.lower() == "man":
    Vocht = 0.72
elif Gender.lower() == "vrouw":
    Vocht = 0.61


a = Glazen*10
b = Massa*Vocht
c = Tijd-0.5
d = Massa*0.002
e = a/b

Promille = e-c*d

print(Promille,"‰")

print(((Glazen*10)/(Massa*Vocht))-((Tijd-0.5)*(Massa*0.002)))