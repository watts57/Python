
import datetime

# source for pricing information: https://www.alabamapower.com/residential/residential-pricing-and-rates/standard-family-dwelling-rate.html

def kwhCost(kwh):
    #if summer:
    # bill = baseCharge + (increasedRateThreshold * seasonal rate)
    winter = True
    currentDate = datetime.datetime.today()
    currentMonth = currentDate.month
    currentYear = currentDate.year

    if (currentMonth < 5 ) or (currentMonth > 10):
        winter == True
    else:
        winter == False
    print("\nBilling Cycle: " + str(currentMonth) + "/" + str(currentYear) + "\n")
    baseCharge = 14.50

    if winter == False:
        belowThresholdRate = 0.100511  #
        increasedRateThreshold = 1000 # summer kwh threshold for increased prices (residential)
        overThresholdRate = 0.10304 # it's summer, charge this per kwh over increasedRateThreshold
    else:
        belowThresholdRate = 0.100511  #
        increasedRateThreshold = 750 # winter kwh threshold for increased prices (residential)
        overThresholdRate = 0.10304 #it's winter, charge this per kwh over increasedRateThreshold



    kwhOverThreshold = kwh - increasedRateThreshold
    kwhUnderThreshold = kwh - kwhOverThreshold

    if kwhOverThreshold > 0:
        totalBill = baseCharge + (overThresholdRate * kwhOverThreshold) + (belowThresholdRate * kwhUnderThreshold)

        print("Base Charge: " + str(baseCharge))
        print("\n")
        print("kWH Used: \n" + str(kwhUnderThreshold) + " kWH @ " + str(belowThresholdRate)+ " = $"+ str(kwhUnderThreshold * belowThresholdRate)+ "\n"+str(kwhOverThreshold)+"kWH @ "+ str(overThresholdRate) + " = $"+ str(kwhOverThreshold * overThresholdRate))
    else:

        totalBill = baseCharge + (belowThresholdRate * kwh)
        print(str(kwh) + "@ $" + str(belowThresholdRate) + " = $" + str(kwh * belowThresholdRate))
        print("\n")
        print("Base Charge: " + str(baseCharge))
        print("\n")
        print("kWH Used: "+ str(kwh) + " kWH @ " + str(belowThresholdRate))



    print("Total kWH used: " + str(kwh))
    print()
    return totalBill





kwh = int(input("Please input the number of KWH: "))



print("\nYour Monthly Bill : \n")
print("Total: $"+str(round(kwhCost(kwh),2)))


