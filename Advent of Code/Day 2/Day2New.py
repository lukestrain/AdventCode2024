# Define and Input lists

# Store all reports in one giant list of the reports (So a list of lists)
reports = []

testReport = [81, 78, 76, 79, 82, 85, 86, 88]

with open('Day 2/input.txt', 'r') as file:
    for line in file:
        report = []
        reportStr = line.split()
        report = [int(item) for item in reportStr]
        reports.append(report)

# Function to check if a report is safe
def isSafe(report):

    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    #print (differences)
    if all(n in [1,2,3] for n in differences) or all(n in [-1,-2,-3] for n in differences):
        return "Safe"
    else:
        return "Unsafe"
    

    
# Function to count safe reports
def countSafe(listOfReports):
    safeCount = 0
    for report in listOfReports:
        if isSafe(report) == "Safe":
            safeCount += 1
    return safeCount



def countSafeDampener(listofReports):
    safeCount = 0
    #dampened = []
    #lineNum = 0
    for report in listofReports:
        if isSafe(report) == "Safe":
            safeCount += 1
        else:
            #print ("Unsafe Report: ", report)
            for i in range(len(report)):
                tempReport = report.copy()
                tempReport.pop(i)
                if isSafe(tempReport) == "Safe":
                    safeCount +=1
                    #dampened.append(lineNum)
                    break
        #lineNum += 1
    return safeCount
                

# Test with the reports
print(countSafeDampener(reports))
# print(countSafeDampener(reports))
# Example data for testing
# exampleList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
exampleReports = [[5,6, 7, 10, 13, 16, 13]] #[16, 18, 20, 21, 23, 25, 29]]
#, [44, 46, 48, 49, 52, 55, 56, 62]]

#print(countSafeDampener(exampleReports))
# print("ExampleReports")
# print(countSafeDampener(exampleReports))
