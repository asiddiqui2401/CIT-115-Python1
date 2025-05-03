MERCURY = 0.38
VENUS =0.91
MOON = 0.165
MARS = 0.38
JUPITER = 2.34
SATURN = 0.93
URANUS = 0.92
NEPTUNE = 1.12
PLUTO = 0.066

sName = input("What is your name: ")
fWeight = float(input("What is your weight on earth: "))

fMercury_Weight = fWeight* MERCURY

fVenus_Weight = fWeight* VENUS

fMoon_Weight = fWeight* MOON

fMars_Weight = fWeight* MARS

fJupiter_Weight = fWeight* JUPITER

fSaturn_Weight = fWeight* SATURN

fUranus_Weight = fWeight* URANUS

fNeptune_Weight = fWeight* NEPTUNE

fPluto_Weight = fWeight* PLUTO
print(f"Your Name: {sName}")
print(f"Weight on Earth :{fWeight}")
print(f"{sName}, Your Weight on other Planets is:")
print(f"{'Weight on Mercury:':20}{fMercury_Weight:10.2f}")
print(f"{'Weight onvenus :':20}{fVenus_Weight:10.2f}")
print(f"{'Weight on moon:':20}{fMoon_Weight:10.2f}")
print(f"{'Weight on Mars:':20}{fMars_Weight:10.2f}")
print(f"{'Weight on Jupiter:':20}{fJupiter_Weight:10.2f}")
print(f"{'Weight on Saturn:':20}{fSaturn_Weight:10.2f}")
print(f"{'Weight on Uranus:':20}{fUranus_Weight:10.2f}")
print(f"{'Weight on Neptune:':20}{fNeptune_Weight:10.2f}")
print(f"{'Weight on Pluto:':20}{fPluto_Weight:10.2f}")










