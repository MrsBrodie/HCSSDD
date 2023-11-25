#function to open and read the file


def readDetails():
    itemsarray = [None] * 200
    pricesarray = [None] * 200
    counter = 0

    with open("PlantStockFile.csv") as readfile:
        #read the first line of the file
        line = readfile.readline().rstrip('\n')
        #while this line has a value (there is soome text)
        while line:
            #split the file on each comma
            items = line.split(",")
            #first element has the licence
            itemsarray[counter] = items[0]
            #second element has the date
            pricesarray[counter] = items[1]
            counter += 1
            line = readfile.readline().rstrip('\n')
        input("File read complete, please press enter")
        return itemsarray, pricesarray


def searchFile(names):
    searchitem = input("Please enter the item being searched for")

    #Loop through the entire array
    for x in range(len(names)):
        #If item is found
        if names[x] == searchitem:
            print("Item found in aisle " + str(x + 1))


def main():
    items, prices = readDetails()
    searchFile(items)


main()
