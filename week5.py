from math import sqrt
sayi=14
def sayi_asal_mi(sayi):
    i=3

    if(sayi<2):
        return 0

    if(sayi !=2 and sayi%2==0):
        return 0
    while (i<=sayi ** (1/2)):
        if(sayi%i==0):
            return 0
        i +=2
    return 1
def sayi_asal_carpan(sayi):
    liste = []
    if(sayi_asal_mi(sayi)):
        return "sayi asal"

    else:
        for i in range(2,sayi+1):
            if (sayi % i == 0):
                if(sayi_asal_mi(i)):
                    liste.append(i)

        return liste
print(sayi_asal_carpan(sayi))
liste=[4,-3,2,-1,-2,6,-5]
def liste_ardasik_toplam(liste):
    dizi=[]
    i=2
    while(i <= len(liste)):
        for j in range(0,len(liste)+1):
            dizi.append(sum(liste[j:i]))
        i+=1
    return max(dizi)
print(liste_ardasik_toplam(liste))