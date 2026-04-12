table = [["U", "V", "W", "X", "Y"],
               ["P", "Q", "R", "S", "T"],
               ["K", "L", "M", "N", "O"],
               ["F", "G", "H", "I", "J"],
               ["A", "B", "C", "D", "E"]]
user_input = input("Enter your word with a max length of 10 letters and a min length of 1 letter: \n").upper()
def coordinates(word, table):
       cellsize = 5 ** len(word)
       row = 0
       column = 0       
       for char in word:
              cellsize = cellsize // 5
              char_row = 1
              char_column = 1           
              for i in range(5):
                     for j in range(5):
                            if table[i][j] == char:
                                   char_row = i
                                   char_column = j
                                   break
                     if char_row != 1:
                            break              
              row = row + (char_row * cellsize)
              column = column + (char_column * cellsize)
       row = row + cellsize // 2
       column = column + cellsize // 2
       return row, column
nums = coordinates(user_input, table)
print(nums[1]+1, nums[0]+1)