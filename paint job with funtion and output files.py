from math import ceil

def getFloatInput(sPrompt):
    while True:
        try:
            fValue = float(input(sPrompt))
            if fValue <= 0:
                raise ValueError
            return fValue
        except ValueError:
            print("Please enter a number greater than zero.")           
            
def getGallons0fPaint(fSqFeet, fFtPerGallon):
    return ceil(fSqFeet / fFtPerGallon)
def getLaborHours(fHoursPerGallon, iTotalGallons):
    return fHoursPerGallon * iTotalGallons
def getLaborCost(fHoursPerGallon, fLaborPerHr):
    return fHoursPerGallon * fLaborPerHr
def getPaintCost(iTotalGallon, fPaintPrice):
    return iTotalGallon * fPaintPrice

def getStateTax(sState):
    if sState == 'CT' or sState == 'VT':
        return 0.06
    elif sState == 'MA':
        return 0.0625
    elif sState == 'ME':
        return 0.085
    elif sState == 'RI':
        return 0.07
    elif sState == 'NH':
        return 0.0
    else:
        return 0.0
    
def showCostEstimate(iTotalGallons, fTaxRate, sLastName, fTotalPaint, fLaborCost, fTotalLaborHr):
    
    fTotalLaborCharge = fLaborCost * iTotalGallons
    fTotalTax = fTaxRate * (fTotalLaborCharge + fTotalPaint)
    fTotalCost = fTotalTax + fTotalLaborCharge + fTotalPaint
    sFileName = f"{sLastName} Paintjob0utput.txt"
      
    print(f"Customer:{sLastName}")
    print(f"Gallons of Paint:{iTotalGallons}")
    print(f"Hours of Labor:{fTotalLaborHr}")
    print(f"Paint Charges: ${fTotalPaint:,.2f}")
    print(f"Labour Charges: ${fTotalLaborCharge:,.2f}")
    print(f"Tax: ${fTotalTax:,.2f}")
    print(f"Total Cost: ${fTotalCost:,.2f}")
    
    with open(sFileName, "w") as f:
        f.write(f"Customer:{sLastName}/n")
        f.write(f"Gallons of Paint:{iTotalGallons}/n")
        f.write(f"Hours of Labour:{fTotalLaborHr}/n")
        f.write(f"Paint Charges: ${fTotalPaint:,.2f}/n")
        f.write(f"Labour Charges: ${fTotalLaborCharge:,.2f}/n")
        f.write(f"Tax: ${fTotalTax:,.2f}/n")
        f.write(f"Total Cost: ${fTotalCost:,.2f}/n")
        
    print(f"File:{sFileName} was created.")
    
def main():
    print("Welcome to the Paint Job Estimator\n")

    fSqFeet = getFloatInput("Enter square feet of wall:")
    fPaintPrice = getFloatInput("Enter price per gallon:")
    fFtPerGallon = getFloatInput("Enter feet per gallon:")
    fHoursPerGallon = getFloatInput("Enter how many labour per hours:")
    fLaborPerHr = getFloatInput("Enter labour cost per hours:")
       
    sState = input("Enter the initials for the state :").upper()
    sLastName = input("Enter the last name of the client:").title()
    
    iTotalGallons = getGallons0fPaint(fSqFeet, fFtPerGallon)
    iTotalLaborHr = getLaborHours(fHoursPerGallon, iTotalGallons)
    fLaborCost = getLaborCost(fHoursPerGallon, fLaborPerHr)
    fTotalPaint = getPaintCost(iTotalGallons, fPaintPrice)
    fTaxRate = getStateTax(sState)

    showCostEstimate(iTotalGallons,
        fTaxRate,
        sLastName,
        fTotalPaint,
        fLaborCost,
        iTotalLaborHr,
        )
main()
    

    

    

    
            
