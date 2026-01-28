# Q1:
# a:
import math
def round_up_2dp(x):
    return math.ceil(x * 100) / 100
repaid = 100
interest = int(input("Enter the interest percentage: \n"))
repayment = int(input("Enter the repayment percentage: \n"))
debt = 100
counter = 0
while debt > 0:
    counter += 1
    interest_charged = debt * (interest / 100)
    debt += interest_charged
    repaid += interest_charged
    debt = round_up_2dp(debt)
    repayment_charge = debt * (repayment / 100)
    repayment_charge = round_up_2dp(repayment_charge)
    if repayment_charge > 50:
        debt -= repayment_charge
    else:
        if debt < 50:
            debt = 0
        else:
            debt -= 50
    repaid = round_up_2dp(repaid)
print(repaid)
print(counter)

# b: 5
# c: 100 percent interest for 1 percent repayment

# Q3:
def get_neighbors(serial):
    neighbors = []
    digits = list(serial)
    for i in range(len(digits) - 1):
        val_i = int(digits[i])
        val_i_plus_1 = int(digits[i + 1])
        between = min(val_i, val_i_plus_1) + 1
        max_between = max(val_i, val_i_plus_1)         
        for j in range(len(digits)):
            if j != i and j != i + 1:
                if between <= int(digits[j]) < max_between:
                    digits[i], digits[i + 1] = digits[i + 1], digits[i]
                    neighbors.append(''.join(digits))
                    digits[i], digits[i + 1] = digits[i + 1], digits[i]
                    break    
    return neighbors

def max_distance(serial):
    visited = {serial}
    queue = deque([(serial, 0)])
    max_dist = 0
    while queue:
        current, dist = queue.popleft()
        max_dist = max(max_dist, dist)
        
        for neighbor in get_neighbors(current):
            if neighbor not in visited: 
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))    
    return max_dist

d = int(input("Enter the number of digits: \n"))
serial = input("Enter the serial number: \n")
print(max_distance(serial))
