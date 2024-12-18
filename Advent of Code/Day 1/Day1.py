#Define and Input lists

list1 = []
list2 = []

with open('Day 1\input.txt', 'r') as file:
    for line in file:
        values = line.split()

        list1.append(int(values[0]))
        list2.append(int(values[1]))

#Sort the lists
list1Sorted = sorted(list1)
list2Sorted = sorted(list2)


def Part1(listA, listB):
    #Determine the Total Distance between the sorted lists
    #Create list of differences
    distances = []

    for i in range(len(listA)):
        d =  listA[i] - listB[i]
        #Check for negative number since I am not checking which is greater between list 1 and list 2
        if d < 0:
            d = d * -1
        distances.append(d)

    totalDistance = 0

    for i in distances:
        totalDistance += i

    return totalDistance

print(Part1(list1Sorted, list2Sorted))


def Part2(listA, listB):
    #Determines the Similarity Score
    simScore = 0

    for i in range(len(listA)):
        #For each item in List A, I will count the occurances in List B that match it, then use the similarty score fomula to add that to the simScore variable
        listItem = listA[i]
        occurances = 0
        for j in range(len(listB)):
            if listB[j] == listItem:
                occurances += 1
        simScore += (listItem * occurances) 

    return simScore


print (Part2(list1,list2))