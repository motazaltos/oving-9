# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 01:46:02 2021

@author: motaz
"""

class Flervalgsspørsmål:
    def __init__(self, spørsmål, alternativer, svar=0):
        self.spørsmål = spørsmål
        self.alternativer = alternativer
        self.svar = svar
        self.svar_tekst = self.alternativer[int(self.svar)]
        
    def __str__(self):
        resultat = self.spørsmål + "\nSvaralternativer:\n"
        for index, verdi in enumerate(self.alternativer):
            resultat += f"{index}: {verdi}\n"
        return resultat
    
    def sjekk_svar(self, svaret):
        print(svaret, self.svar)
        if int(svaret) == self.svar:
            return True
        else:
            return False

    def korrekt_svar_sjekk(self, brukersvar):
        if self.svar != brukersvar:
            return self.svar
    def korrekt_svar_tekst(self):
        return f"svaret er: {self.svar_tekst}"
    
    
#Oppg 9)

questions = []

with open("sporsmaalsfil.txt", "r", encoding="UTF8") as fil:
    for linje in fil:
        hele = linje.split(":")
        Flervalgs = hele
        altern = hele[2]
        delt = altern.split(",")
        questions.append(Flervalgsspørsmål(hele[0], delt, hele[1].strip()))
        






if __name__ == "__main__": 
    spiller_1_poeng = 0
    spiller_2_poeng = 0
    for spørsmål in questions:
        print(spørsmål)
        print(spørsmål.svar)
        bs1 = input("spiller 1: ")
        bs2 = input("spiller 2: ")
        riktig1 = spørsmål.sjekk_svar(bs1)
        print(riktig1)
        
        
        if riktig1 == True:
            spiller_1_poeng += 1
            print("rett svar")
        riktig2 = spørsmål.sjekk_svar(bs2)
        if riktig2 == True:
            spiller_2_poeng += 1
            print("rett svar")
        print(spørsmål.svar_tekst)

    print(spiller_1_poeng)
    print(spiller_2_poeng)
    