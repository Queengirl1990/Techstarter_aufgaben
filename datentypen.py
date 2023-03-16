kleiderschrank = ["Hose", "T-Shirt", "Kleid"]
print (type(kleiderschrank))
print (kleiderschrank)
kleiderschrank.append("Pullover")
for sachen in kleiderschrank : 
    print(sachen) 

kommode = ["Schuhe" , "Socken" , "Mütze"]
print (type(kommode))
print (kommode)
for sachen in kommode : 
    print(sachen) 

print ("")
print ("Kommode aus Platzmangel verkauft")
kleiderschrank += kommode
for sachen in kleiderschrank : 
    print(sachen) 