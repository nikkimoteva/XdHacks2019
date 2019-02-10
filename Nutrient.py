from urllib.request import urlopen
from bs4 import BeautifulSoup

url_base = "https://www.canada.ca/en/health-canada/services/food-nutrition/healthy-eating/nutrient-data/nutrient-value-some-common-foods-2008.html#a8"

fruit_list = {}
veggie_list = {}

def parse_url(url):
   html_page = urlopen(url)
   soup = BeautifulSoup(html_page, 'html.parser')
   return soup

# Gets name of professor-> string, string
def get_fruits(soup):
   something = soup.find('table', {'id': 'a8'})
   find_title = something.find('tbody')
   find_list = find_title.find_all('tr')
   for row in find_list:
       cols = row.find_all('td')
       cols = [x.text.strip() for x in cols]
       items = {}
       if len(cols) > 1:
           title = cols[0]
           items['Sugar'] = str(cols[7])
           items['Calcium'] = str(cols[10])
           items['Iron'] = str(cols[11])
           items['Sodium'] = str(cols[12])
           items['Potassium'] = str(cols[13])
           fruit_list[title] = items



def get_veggies(soup):
   something = soup.find_all('table', class_= 'subject fontSize75 table-bordered table')
   find_title = something[1].find('tbody')
   find_list = find_title.find_all('tr')
   for row in find_list:
       cols = row.find_all('td')
       cols = [x.text.strip() for x in cols]
       items = {}
       if len(cols) > 1:
           title = cols[0]
           items['Sugar'] = str(cols[7])
           items['Calcium'] = str(cols[10])
           items['Iron'] = str(cols[11])
           items['Sodium'] = str(cols[12])
           items['Potassium'] = str(cols[13])
           veggie_list[title] = items

def findBest(listOfDefects, category):
    list = []
    proceed = False
    listLength = len(listOfDefects)
    for stuff in listOfDefects:
        i = 0
        if len(list) != 0:
            proceed = True
        for singleVeg in category:
            if category[singleVeg][stuff] == 'tr' or category[singleVeg][stuff] == 'N/A':
                value = 0
            else:
                value = float(category[singleVeg][stuff])
            if proceed:
                curTuple = (list[i][0], list[i][1] + value)
                list[i] = curTuple
            else:
                curTuple = (singleVeg, value)
                list.append(curTuple)
            i = i + 1

    k = 0
    while k < len(list):
        reduced = round(list[k][1] / listLength, 2)
        curTuple = (list[k][0], reduced)
        list[k] = curTuple
        k = k + 1
        mergeSort(list)

    return list

def mergeSort(toBeSorted):
    if len(toBeSorted) > 1:
        mid = len(toBeSorted) // 2
        left = toBeSorted[:mid]
        right = toBeSorted[mid:]
        mergeSort(left)
        mergeSort(right)
        leftCounter = 0
        rightCounter = 0
        totalCounter = 0

        while leftCounter < len(left) and rightCounter < len(right):
            if left[leftCounter][1] < right[rightCounter][1]:
                toBeSorted[totalCounter] = left[leftCounter]
                leftCounter = leftCounter + 1
            else:
                toBeSorted[totalCounter] = right[rightCounter]
                rightCounter = rightCounter + 1
            totalCounter = totalCounter + 1


        while leftCounter < len(left):
            toBeSorted[totalCounter] = left[leftCounter]
            leftCounter = leftCounter + 1
            totalCounter = totalCounter + 1


        while rightCounter < len(right):
            toBeSorted[totalCounter]=right[rightCounter]
            rightCounter = rightCounter + 1
            totalCounter = totalCounter + 1


def nutrientInit(stuff, value):
    notsoup = parse_url(url_base)
    get_fruits(notsoup)
    get_veggies(notsoup)
    input_list = [stuff]
    # list = getInformation()
    # counter = 0
    # while counter < 5:
    #     if list[counter][3] > 0:
    #         input_list.append(list[counter][0])
    #     counter = counter + 1

    # print(input_list)
    bestVeggiesList = findBest(input_list, veggie_list)
    bestFruitsList = findBest(input_list, fruit_list)
    bestFruitsList = bestFruitsList[:5]
    bestVeggiesList = bestVeggiesList[:5]
    newFruitsList = []
    newVeggiesList = []
    i = 0
    while i < value:
        newFruitsList.append(bestFruitsList[i][0])
        newVeggiesList.append(bestVeggiesList[i][0])
        i = i + 1

    finalList = [newFruitsList, newVeggiesList]
    return finalList