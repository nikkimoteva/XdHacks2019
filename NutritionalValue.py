# Author: Nikki Motevaselolhagh
# Date: Feb 10, 2018
# Purpose: parse the data, give information on the serving size

file = open("data.txt", "r")


#Information Indices
# 0 : food_code
# 1 : food_description
# 2 : measure_name

code = list()
desc = list()
measure = list()

def info():
    code_keyword = "food_code"
    desc_keyword = "food_description"
    measure_keyword = "measure_name"
    for line in file:
        if code_keyword in line:
            code.insert(0, code_keyword)
            code.insert(1, int(line.partition(code_keyword + " ")[2].partition(" ")[0]))
        if desc_keyword in line:
            desc.insert (0, line.partition(desc_keyword)[1])
            desc.insert(1, str(line.partition(desc_keyword + " ")[2].partition(" ")[0]))
        if measure_keyword in line:
            measure.insert(0, line.partition(measure_keyword)[1])
            measure.insert(1, str(line.partition(measure_keyword + " ")[2].partition(" ")[0]))

    print(code)
    print(desc)
    print(measure)

info()



