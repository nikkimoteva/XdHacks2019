file = open("C:/Users/Andrew/Desktop/Report.txt", "r")
#print(file.read())

# Information Indices
# 0 = Title
# 1 = Current value measured in person
# 2 = Difference indicator
potassium = list()
sodium = list()
iron = list()
calcium = list()
glucose = list()

def getInformation():
    potassium_keyword = "Potassium"
    sodium_keyword = "Sodium"
    iron_keyword = "Ferritin"
    calcium_keyword = "Calcium"
    glucose_keyword = "Glucose Fasting"

    for line in file:
        if potassium_keyword in line:
            potassium.insert(0, line.partition(potassium_keyword)[1])
            potassium.insert(1, float(line.partition(potassium_keyword + " ")[2].partition(" ")[0]))
            rangeString = line.partition(potassium_keyword + " ")[2].partition(" ")[2].partition(" ")[0]
            range_lower = float(rangeString.partition("-")[0])
            range_upper = float(rangeString.partition("-")[2])
            if (potassium[1] <= range_upper and potassium[1] >= range_lower):
                potassium.insert(2, float(0))
            elif (potassium[1] - range_upper > 0):
                potassium.insert(2, float((potassium[1]-range_upper)/range_upper))
            else:
                potassium.insert(2, float((potassium[1]-range_lower)/range_lower))

        if sodium_keyword in line:
            sodium.insert(0, line.partition(sodium_keyword)[1])
            sodium.insert(1, float(line.partition(sodium_keyword + " ")[2].partition(" ")[0]))
            rangeString = line.partition(sodium_keyword + " ")[2].partition(" ")[2].partition(" ")[0]
            range_lower = float(rangeString.partition("-")[0])
            range_upper = float(rangeString.partition("-")[2])
            if (sodium[1] <= range_upper and sodium[1] >= range_lower):
                sodium.insert(2, float(0))
            elif (sodium[1] - range_upper > 0):
                sodium.insert(2, float((sodium[1]-range_upper)/range_upper))
            else:
                sodium.insert(2, float((sodium[1]-range_lower)/range_lower))

        if glucose_keyword in line:
            glucose.insert(0, "Sugar")
            glucose.insert(1, float(line.partition(glucose_keyword + " ")[2].partition(" ")[0]))
            rangeString = line.partition(glucose_keyword + " ")[2].partition(" ")[2].partition(" ")[0]
            range_lower = float(rangeString.partition("-")[0])
            range_upper = float(rangeString.partition("-")[2])
            if (glucose[1] <= range_upper and glucose[1] >= range_lower):
                glucose.insert(2, float(0))
            elif (glucose[1] - range_upper > 0):
                glucose.insert(2, float((glucose[1]-range_upper)/range_upper))
            else:
                glucose.insert(2, float((glucose[1]-range_lower)/range_lower))

        if iron_keyword in line:
            iron.insert(0, "Iron")
            iron.insert(1, float(line.partition(iron_keyword + " ")[2].partition(" ")[0]))
            rangeString = line.partition(iron_keyword + " ")[2].partition(" ")[2].partition(" ")[0]
            range_lower = float(rangeString.partition("-")[0])
            range_upper = float(rangeString.partition("-")[2])
            if (iron[1] <= range_upper and iron[1] >= range_lower):
                iron.insert(2, float(0))
                if (iron[1] < 50):
                    iron.insert(3, "Probable Iron Deficiency")
                elif (iron[1] < 100):
                    iron.insert(3, "Possible Iron Deficiency")
            elif (iron[1] - range_upper > 0):
                iron.insert(2, float((iron[1]-range_upper)/range_upper))
            else:
                iron.insert(2, float((iron[1]-range_lower)/range_lower))

        if calcium_keyword in line:
            calcium.insert(0, line.partition(calcium_keyword)[1])
            calcium.insert(1, float(line.partition(calcium_keyword + " ")[2].partition(" ")[0]))
            rangeString = line.partition(calcium_keyword + " ")[2].partition(" ")[2].partition(" ")[0]
            range_lower = float(rangeString.partition("-")[0])
            range_upper = float(rangeString.partition("-")[2])
            if (calcium[1] <= range_upper and calcium[1] >= range_lower):
                calcium.insert(2, float(0))
            elif (calcium[1] - range_upper > 0):
                calcium.insert(2, float((calcium[1]-range_upper)/range_upper))
            else:
                calcium.insert(2, float((calcium[1]-range_lower)/range_lower))
    file.close()

def getPotassium():
    print(potassium)
    return potassium

def getSodium():
    print(sodium)
    return sodium

def getIron():
    print(iron)
    return iron

def getGlucose():
    print(glucose)
    return glucose

def getCalcium():
    print(calcium)
    return calcium

getInformation()
getPotassium()
getCalcium()
getSodium()
getIron()
getGlucose()