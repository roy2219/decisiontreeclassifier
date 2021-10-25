import csv

### Gets the Data
def readData():
    with open('Data/Calculating GINI - Data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        data = []
        ### Getting the data
        for line in csv_reader:
            data.append(line)
    return data
### Gets the Data Types
def getDataType():
    data = readData()
    dataTypes = []
    for column in data[1]:
        try:
            value = int(column)
            dataTypes.append('int')
        except:
            dataTypes.append('str')
    return dataTypes

### Sorts all the values, needs to be finished
def sortValues():
    data = readData()
    headers = getDataType()
    sortedData = []
    integerPositions = []
    for index,value in enumerate(headers):
        if 'int' in value:
            integerPositions.append(index)
    for index in integerPositions:
        toBeSorted = []
        for dataPoint in range(len(data)):
            toBeSorted.append(data[dataPoint][index])
        sortedData.append(sorted(toBeSorted, reverse=True))
    orderedIndex = []
    for index, sublist in enumerate(sortedData):
        for value in sublist:
            temp = []
            for index2, sublist2 in enumerate(data):
                try:
                    print(sublist2.index(value))
                    # print(f"List{index2}")
                    temp.append(index2)
                except:
                    continue
                orderedIndex.append(temp)
    return orderedIndex
                    

def printValues():
    indexes = sortValues()
    data = readData()
    



### Now I need to get the positions of these values in the original data          

    


if __name__=="__main__":
    printValues()