
num = int(input("Enter your number: \n"))
rd_count = 0
for n in range(1, num + 1):
    new_num = str(n)
    length = len(new_num)
    rd = True
    larger_count = 0    
    for i in range(length - 1, 0, -1):
        if new_num[i] > new_num[i - 1]:
            larger_count = larger_count + 1  
    if larger_count == 1:
        rd_count = rd_count + 1
rd_count = rd_count + 9
print(rd_count)
