print(" *** Wind classification ***")
inp = float(input("Enter wind speed (km/h) : "))
if inp <= 51.99:
    print("Wind classification is Breeze.")
elif inp > 51.99 and inp <= 55.99:
    print("Wind classification is Depression.")
elif inp > 55.99 and inp <= 101.99:
    print("Wind classification is Tropical Storm.")
elif inp > 101.99 and inp <= 208.99:
    print("Wind classification is Typhoon.")
elif inp >= 209:
    print("Wind classification is Super Typhoon.")
else:
    print("Incorrect Input")
