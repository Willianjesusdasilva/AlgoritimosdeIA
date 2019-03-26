from fuzzywuzzy import fuzz
from fuzzywuzzy import process


t1 = open("text1.txt","r")
l1 = t1.readlines()
t1.close()
t2 = open("text2.txt","r")
l2 = t2.readlines()
t2.close()


result = fuzz.partial_ratio(str(l1),str(l2))
print('Porcentagem de semelhança: '+ str(result))