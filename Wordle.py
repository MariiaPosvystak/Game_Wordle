from colorama import Fore, Back, Style
import random 
print("Game Wordle")
print("Mängu eesmärk on arvata 5-täheline sõna, mida arvuti mõtleb")
while True:
    valik=input("Kas soovite mängida? (jah/ei)")
    if valik=="jah":
        word=["parem","vasak","jalad","valge","musta","kassa","tütar","algus","tugev","saama","kooli","vanus","lahti"]
        tähestik=("q w e r t y u i o p ü õ\n"
                  "a s d f g h j k l ö ä\n"
                  "z x c v b n m")
        word_1=random.choise(word)
        word_list=list(word_1)
        for a in range (6):
            result=" "
            print(f"Katse {a+1}/6")
            print(tähestik)
            while 1:
                try:
                    sõne=str(input("Sisestage 5-täheline sõna: ")).lower()
                    if sõne.isalpha() and len(sõne)==5:
                        break
                    else:
                        print("Kirjutage sõna ainult väikeste tähtedega ja sõna pikkus on 5 tähte!")
                except:
                    print("Kirjutage sõna ainult väikeste tähtedega ja sõna pikkus on 5 tähte!")
            sõne_list=list(sõne)
            for b in range (5):
                if sõne_list[b]==word_list[b]:
                    result+=Fore.GREEN + sõne_list[b]+Style.RESET_ALL
                elif sõne_list[b] in word_list and sõne_list[b] != word_list:
                    result+=Fore.YELLOW +sõne_list[b]+Style.RESET_ALL
                else:
                    result+="-"
            result+="\n"
            print(result)
            if sõne==word_1:
                print(f"Palju õnne, te võitsite! Mõeldud sõna on: {word_1}")
                break
        else:
            print(f"Te kaotasite! Mõeldud sõna on: {word_1}")
    elif valik=="ei":
        print("Mäng on lõppenud")
        break