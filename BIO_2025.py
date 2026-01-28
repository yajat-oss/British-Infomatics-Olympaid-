def is_palindrome(n):
    return str(n) == str(n)[::-1]

def one_palindrome(num):
    if is_palindrome(num):
        return num
    return False

def two_palindrome(num):
    for num_1 in range(1, num):
        if is_palindrome(num_1):
            num_2 = num - num_1
            if num_2 > 0 and is_palindrome(num_2):
                return num_1, num_2
    return False

def three_palindromes(num):
    for num_1 in range(1, num):
        if is_palindrome(num_1):
            for num_2 in range(1, num - num_1):
                if is_palindrome(num_2):
                    num_3 = num - num_1 - num_2
                    if num_3 > 0 and is_palindrome(num_3):
                        return num_1, num_2, num_3
    return False
num = int(input("Enter the number that should be made into a palindromic sum: \n"))
result = one_palindrome(num)
if not result:
    result = two_palindrome(num)
    if not result:
        result = three_palindromes(num)
print(result)