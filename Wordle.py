from colorama import Fore, Back, Style
import random 
print(+ACI-Game Wordle+ACI-)
print(+ACI-M+AOQ-ngu eesm+AOQ-rk on arvata 5-t+AOQ-heline s+APU-na, mida arvuti m+APU-tleb+ACI-)
while True:
    valik+AD0-input(+ACI-Kas soovite m+AOQ-ngida? (jah/ei)+ACI-)
    if valik+AD0APQAi-jah+ACI-:
        word+AD0AWwAi-parem+ACI-,+ACI-vasak+ACI-,+ACI-pahad+ACI-,+ACI-jalad+ACI-,+ACI-valge+ACI-,+ACI-musta+ACI-,+ACI-kassa+ACI-,+ACI-t+APw-tar+ACI-,+ACI-agus+ACI-,+ACI-tugev+ACI-,+ACI-saama+ACI-,+ACI-kooli+ACI-,+ACI-vanus+ACI-,+ACI-lahti+ACIAXQ-
        t+AOQ-hestik+AD0-(+ACI-q w e r t y u i o p +APw- +APU- +AFw-n+ACI-
                    +ACI-a s d f g h j k l +APY- +AOQ- +AFw-n+ACI-
                    +ACI-z x c v b n m+ACI-)
        word+AF8-1+AD0-random.choise(word)
        word+AF8-list+AD0-list(word+AF8-1)
        for a in range (6):
            result+AD0AIgAi-
            print(f+ACI-Katse +AHs-a+-1+AH0-/6+ACI-)
            print(t+AOQ-hestik)
            while 1:
                try:
                    s+APU-ne+AD0-str(input(+ACI-Sisestage 5-t+AOQ-heline s+APU-na: +ACI-)).lower()
                    if s+APU-ne.isalpha() and len(s+APU-ne)+AD0APQ-5:
                        break
                    else:
                        print(+ACI-Kirjutage s+APU-na ainult v+AOQ-ikeste t+AOQ-htedega ja s+APU-na pikkus on 5 t+AOQ-hte+ACEAIg-)
                except:
                    print(+ACI-Kirjutage s+APU-na ainult v+AOQ-ikeste t+AOQ-htedega ja s+APU-na pikkus on 5 t+AOQ-hte+ACEAIg-)
            s+APU-ne+AF8-list+AD0-list(s+APU-ne)
            for b in range (5):
                if s+APU-ne+AF8-list+AFs-b+AF0APQA9-word+AF8-list+AFs-b+AF0-:
                    result+-+AD0-Fore.GREEN +- s+APU-ne+AF8-list+AFs-b+AF0AKw-Style.RESET+AF8-ALL
                elif s+APU-ne+AF8-list+AFs-b+AF0- in word+AF8-list and s+APU-ne+AF8-list+AFs-b+AF0- +ACEAPQ- word+AF8-list:
                    result+-+AD0- Fore.YELLOW +- s+APU-ne+AF8-list+AFs-b+AF0AKw-Style.RESET+AF8-ALL
                else:
                    result+-+AD0AIg--+ACI-
            result+-+AD0AIgBc-n+ACI-
            print(result)
            if s+APU-ne+AD0APQ-word+AF8-1:
                print(f+ACI-Palju +APU-nne, te v+APU-itsite+ACE- M+APU-eldud s+APU-na on: +AHs-word+AF8-1+AH0AIg-)
                break
        else:
            print(f+ACI-Te kaotasite+ACE- M+APU-eldud s+APU-na on: +AHs-word+AF8-1+AH0AIg-)
    elif valik+AD0APQAi-ei+ACI-:
        print(+ACI-M+AOQ-ng on l+APU-ppenud+ACI-)
        break