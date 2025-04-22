import re

result = dir(re)
print(result)


"""
Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times 
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times 
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end

"""

#re module

str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

#re.findall

result = re.findall("Python", str)

print(result)
print(len(result))
print(str.count("Python"))


#re.split

result1 = re.split(" ", str)
print(result1)



#re.sub

result2 = re.sub(" ", "-", str) #bütün boşluk karakterlerini tire ile değiştir
print(result2)

result3 = re.sub("\s", "-", str) #bütün boşluk/match any whitespace karakterlerini tire ile değiştir
print(result3)


#♥re.search

result4 = re.search("Python", str)
print(result4) # match objesi : <re.Match object; span=(0, 6), match='Python'>

result5 = result4.span()
print(result5) #♣string içinde konumunu veriyor

result6 = result4.start()
print(result6) #♠str içinde sıfırıncı karakterden başladığını söylüyor

result7 = result4.end()
print(result7) #str içinde hangi karakterde bitiyor

result8 = result4.group()
print(result8) #bulduğumuzu bize geri gönderir

result9 =  result4.string
print(result9) # arama hangi string kullanıldı



#[a-z] köşeli parantez içine yazılan bütün karakterler aranır
reg = re.findall("[abc]" , str) #köseli parantez içinde str'de bulduğu karakterler 
print(reg)


reg1 = re.findall("[sat]" , str) 
print(reg1)

reg2 = re.findall("[a-e]" , str) 
print(reg2)

reg3 = re.findall("[1-5]" , str) 
print(reg3)

#[0-39] => [01239]

reg4 = re.findall("[^abc]", str) #abc dışında bütün karakterler 
print(reg4)


# . herhangi bir karakteri ifade eder.

reg5 = re.findall("...", str)
print(reg5)

reg6 = re.findall("Py..on", str)
print(reg6)

# ^ carot - belirtilen string karakterle başlıyor mu?

reg7 = re.findall("^P", str)
print(reg7)


# $ belirtilen karakterle bitiyor mu?

reg8 = re.findall("t$", str)
print(reg8)

reg9 = re.findall("saat$", str)
print(reg9)


# * bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder  , a* mn , man , maaan ok


rege = re.findall("sa*t", str)
print(rege)

# + bir karakterin bir ya da daha fazla sayıda olmasını konrol eder, a+ man, maan, maaan

rege1 = re.findall("sa+t", str)
print(rege1)


# ?  bir karakterin sıfır ya da bir kere olmasını kontrol eder

rege2 = re.findall("sa?t", str)
print(rege2)

"""
{} karakter sayısını kontrol eder

al{2}   a karakterinin arkasına l karakteri 2 kez tekrarlanmalı

al{2, 3} a karakterinin arkasına l en az iki, en fazla 3 kez tekrarlanmalı

[0-9]{2,4}  en az 2 en çok 4 basamaklı sayılar


""" 

rege3 = re.findall("a{2}", str) # a'dan bana iki tane olanları getir
print(rege3)


rege4 = re.findall("\Sa{2}.", str) 
print(rege4)


# |  alternatif seçeneklerden bir tanesi , a | b,  cde yok, ade 1 tane, acdbea 3 tane


# () gruplamak için kullanılır (a | b | c)xz  , a,b,c karakterlerinden herhangi biri gelen karakterlerin arkasına xz gelmeli


""" \   özel karakter aramamızı sağlar  \$ normal dolar işareti olarak görür
\A  belirtilen karakter stringin başında mı? 
\Z  belirtilen karakter stringin sonunda mı?
\b belirtilen karakter kelimenin başında mı sonunda mı?
\B belirtilen karakter başında ya da sonunda olmayanlara verir
\w alfabetik karakterler rakamlar alt çizgi karakteri
\W   \w nin tam tersi

"""

rege5 = re.findall("\APython", str)
print(rege5)


rege6 = re.findall("saat\Z", str)
print(rege6)
















































































































