'''Wall Paint
Interior at 18 per square feet and Exterior at 12 per square feet'''

ni=int(input("Number of Interior Walls: "))
ne=int(input("Number of Exterior Walls: "))
nit=0
ext=0
for i in range(ni):
    inte=float(input("Area of Interior Wall: "))
    nit=nit+inte
for j in range(ne):
    exte=float(input("Area of Exterioir Wall: "))
    ext=ext+exte
est=(nit*18)+(ext*12)
print(nit,ext)
print("Total estimate Cost :%.2f"%est)
