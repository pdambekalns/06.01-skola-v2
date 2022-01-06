import mod
paterinsPirms=float(input("Ievadi savu iepriekšējo elektrības skaitītāja rādījumu kilovatstundās! "))
paterinsPec=float(input("ievadi savu esošo elektrības skaitītāja rādījumu kilovatstundās! "))
paterins=paterinsPec-paterinsPirms
ligums=float(input("Ievadi līguma garumu gados"))
print("Par elektrību jāmaksā", mod.maksa(paterins,ligums),"eiro")