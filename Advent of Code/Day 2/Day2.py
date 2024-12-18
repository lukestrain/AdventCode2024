#Define and Input lists

#Store all reports in one giant list of the reports (So a list of lists)
reports = []


testReport = [81,78,76,79,82,85,86,88]

with open('Day 2\input.txt', 'r') as file:
    for line in file:
        report =[]
        reportStr = line.split()
        report = [int(item) for item in reportStr]

        reports.append(report)

def isFirstLowest(report):
    firstNumber = report[0]
    return (all(firstNumber <= number for number in report))

def isFirstHighest(report):
    firstNumber = report[0]
    return (all(firstNumber >= number for number in report))


def isSafe(report):
    #determine if first two items are increasing or decreasing
    reportDirection = ''

    if report[0] > report[1]:
        reportDirection = 'decreasing'
    elif report[0] < report[1]:
        reportDirection = "increasing"
    else:
        return "Unsafe" #Because two numbers can't be the same
    
    #Deal with Decreasing
    if reportDirection == "decreasing":
        for i in range(len(report)-1):
            dif = report[i] - report[i+1]
            if dif not in [1, 2, 3]:
                return "Unsafe"
    else: #Deal with Increasing
        for i in range(len(report)-1):
            dif = report[i] - report[i+1]
            if dif not in [-1, -2, -3]:
                return "Unsafe"
        
    return "Safe"



def isSafeWithDampener(report):

    reportDirection = ''


#Check the first entry for an error
    if isFirstHighest(report) == False and isFirstLowest(report) == False:
        del report[0]
        unsafeCount += 1
        if isFirstHighest(report) == False and isFirstLowest(report) == False:
            return "Unsafe"
        
    #determine if the report is increasing or decreasing
    for i in range(len(report)-1):
        if report[0] > report[i+1]:
            decreaseCount += 1
        elif report[0] < report[i+1]:
            increaseCount += 1
        else:
            equalCount += 1
    if equalCount > 1:
        return "Unsafe"
    if decreaseCount > increaseCount:
        reportDirection = "decreasing"
    else:
        reportDirection = "increasing"
    
    #Deal with Decreasing
    
    if reportDirection == "decreasing":
        i = 0
        while i < (len(report)-1):
            dif = report[i] - report[i+1]
            if dif not in [1, 2, 3]:
                unsafeCount += 1
                del report[i+1]
                dif = report[i] - report[i+1]
                if dif not in [1, 2, 3]:
                    i = -1
            i += 1
            
    else: #Deal with Increasing
        i = 0
        while i < (len(report)-1):
            dif = report[i] - report[i+1]
            if dif not in [-1, -2, -3]:
                unsafeCount += 1
                del report[i+1]
                i = -1
            i += 1
    
    if unsafeCount > 1:
        return "Unsafe"
    else:        
        return "Safe"

def countSafe(listOfReports):
    safeCount = 0
    for report in listOfReports:
        if isSafeWithDampener(report) == "Safe":
            safeCount += 1
    return safeCount

print (countSafe(reports))

exampleList = [0,1,2,3,4,5,6,7,8,9]


# for i in range(len(exampleList)):
#     status = isSafeWithDampener(reports[i+20])
#     print(i+21)
#     print(status)
    

#Figure out how to remove an item from a list
# When i get an unsafe number, instead of just increasing the unsafe count, I need to remove the item from the list and start the safe check script over.
#If I have to do that twice then it's unsafe.