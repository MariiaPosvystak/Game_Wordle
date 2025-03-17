from colorama import Fore, Back, Style
import random 
print("Game Wordle")
word=["parem","vasak","pahad","jalad","valge","musta","kassa","tütar","agus","tugev","saama","kooli","vanus","lahti"]
tähestik=("q w e r t y u i o p ü õ \n"
          "a s d f g h j k l ö ä \n"
          "z x c v b n m")
word_1=random.choise(word)
word_list=list(word_1)
for j in range (6):
    result=""
    print(f"Katse {j+1}/6")
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
    for i in range (5):
        if sõne_list[i]==my_list_random[i]:
            result+=Fore.GREEN + sõne_list[i]+Style.RESET_ALL
        elif sõne_list[i] in my_list_random and sõne_list[i] != my_list_random:
            result+= Fore.YELLOW + sõne_list[i]+Style.RESET_ALL
        else:
            result+="-"
    result+="\n"
    print(result)
    if sõne==my_list:
        print(f"Palju õnne, te võitsite! Mõeldud sõna on: {my_list}")
        break
else:
    print(f"Te kaotasite! Mõeldud sõna on: {my_list}")