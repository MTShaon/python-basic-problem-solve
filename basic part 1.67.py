#WAP to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure

kpa = float(input("enter pressure in kilopascal : "))
psi = kpa/6.89475729
mmhg = kpa * 760 / 101.325
atm = kpa/101.325
print("The pressure in pounds per square inch: ",round (psi,2),"psi")
print("The pressure in millimeter of mercury: " ,round(mmhg,2)," mmhg.")
print("Atmosphere pressure: " ,round(atm,2), "atm.")
