import re

a = ["Prêt Plans", "Prêt 2020", "Bordereau 20-060", "ST100271", "ST100271 F02P01.TIF"]

# print(re.findall("(\d{1})", a))
for i in a:
    if not re.match("(\D*\d{4}\D*)", i):
        print("ok", i)
    else:
        print("non ", i)
