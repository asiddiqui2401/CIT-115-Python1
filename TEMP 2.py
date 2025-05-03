
print("Asma Siddiqui temp converter")
fTemp = float(input("Enter the tempreture: "))
sEnter = input("Is the temp F for Fahrenheit or C for Celsius? ").upper()
if sEnter != "F" or sEnter != "C":
    print("Enter F or C")
if sEnter == "F":
 
   if fTemp >212:
 
      print("Temp can not be >212")
   else:
      fCelsius = (5.0/9) * (fTemp - 32)
      print(f"The celcsius equivalent is: {fCelsius:.1f}")
if sEnter == "C":
    if fTemp >100:
        print("Temp can not be >100")
    else:
         fFahrenheit = (9.0/5.0) * (fTemp + 32)
         print(f"The fFahrenheit equivalent is: {fFahrenheit:.1f}")
   
         
