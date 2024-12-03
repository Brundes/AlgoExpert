def historianHysteria(list1, list2):
    
    list1.sort()
    list2.sort()
    sumDiff = 0

    for num1, num2 in zip(list1, list2):
        
        diff = abs(num1 - num2)
        sumDiff = sumDiff + diff
    
    return sumDiff
  

with open('challenges/day_1_historian_hysteria/input.txt','r') as input:
    linhas = input.readlines()
    #print(linhas)

list1 = []
list2 = []

for l in linhas:
    text = l.split()
    list1.append(int(text[0]))
    list2.append(int(text[1]))

result = historianHysteria(list1, list2)
print("Final result", result)
