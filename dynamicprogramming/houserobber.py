


#house robber problem using dynamic programming in python

#top down

def houseRobberTD(houses, currentIndex, tempDict):
    if currentIndex >= len(houses):
        return 0
    else:
        if currentIndex not in tempDict:
            stealFirstHouse = houses[currentIndex] + houseRobberTD(houses, currentIndex+1)
            skipFirstHouse = houseRobberTD(houses, currentIndex+1, tempDict)
            tempDict[currentIndex] = max(stealFirstHouse, skipFirstHouse)
        return tempDict[currentIndex]

houses = [6,7,1,30,8,2,4]

    #bottom up

def houseRobberBU(houses, currentIndex):
    tempArr = [0]*(len(houses)+2)
    for i in range(len(houses)-1, -1, -1):
        tempArr[i] = max(houses[i]+tempArr[i+2], tempArr[i+1])
    return tempArr[0]

print(houseRobberBU(houses, 0))
