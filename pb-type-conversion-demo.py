"""
    Daire Alanı : ℼr²
    Daire Çevresi 2ℼr

    *Yarı çapı verilen dairenin alan ve çevresini hesaplıyınız.
    (r: 3.14)
"""

pi = 3.14
yariCap = float(input ("yarı çap: "))
alan = pi * (yariCap**2)
cevre = 2 * pi * yariCap

print("alan:",alan)
print ("cevre:", cevre)

print ("alan: " + str(alan) +"  " +  "cevre: "+ str(cevre))
