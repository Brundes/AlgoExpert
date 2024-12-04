def isMonotonic(array):
  isIncreasing = True
  isDecreasing = True

  for i in range(len(array) - 1):
    if array[i] < array[i+1]:
      isDecreasing = False

    elif array[i] > array[i+1]:
      isIncreasing = False

  return isIncreasing or isDecreasing
  

def safeDifferences(array):

  for i in range(len(array) -1):
    result = array[i+1] - array[i]

    if abs(result) < 1 or abs(result) > 3:
      return False

  return True


def redNosedReports(input):
  safeReports = 0

  for report in input:
     if isMonotonic(report) and safeDifferences(report):
       safeReports += 1
    
  return safeReports


## INPUT ORGANIZATION

with open('challenges/day_2_red_nosed_reports/input.txt','r') as input:
  linhas = input.readlines()

input = []
  
for l in linhas:
  arraySplited = l.split()

  numsTransformed = []
  
  for num in arraySplited:
    numsTransformed.append(int(num))
  
  input.append(numsTransformed)

result = redNosedReports(input)
print("Final result:", result)