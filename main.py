import mod
paterins=float(input("Ievadi savu elektrības patēriņu kilovatstundās! "))
ligums=float(input("Ievadi līguma garumu gados"))
print("Par elektrību jāmaksā", mod.maksa(paterins,ligums),"eiro")