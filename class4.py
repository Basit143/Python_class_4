# 


name1 : str = "Abdul Basit"
name2 : str = "Basit Abdul Basit"
name3 : str = "Abdul Dayyan"

print(name1)
print(name2)
print(name3)




# ya old way ha list define karny ka 

# phly left to right indexing hoti 
#           0              1                2              3               4
names = ["Abdul Basit","Abdul Dayyan","Qasim Dayyan","Abbas Dayyan","Ahmad Dayyan"]
#             -5           -4                -3           -2             -1
# ab hum right to left bi indexing kar sakty ha 

print(names[0])
print(names[-5])
print(names[2])
print(names[-3])
print(names[4])
print(names[-1])


# ab hum new way sa list handle kary ga 

from typing import Any 

# phly left to right indexing hoti 
#                        0              1                2              3               4
names_1 : list[Any] = ["Abdul Basit","Abdul Dayyan","Qasim Dayyan","Abbas Dayyan","Ahmad Dayyan"]
#                        -5           -4                -3           -2             -1
# ab hum right to left bi indexing kar sakty ha 

print(type(names_1))
print(type(names_1[-1]))

print(f"mary pyary baba jan {names_1[-4].upper()}😍❤!")


# slicing
#    * variable ka bad `names[start:end:step]`
#    * start : int = include
#    * end    : int = n-1
#    * step  : int = sequence

chr : list[str] = list("ABCDEFGHIJKLOMNPQRSTUVWXYZ")

print(chr)



#                   0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19    20  21   22   23   24   25     
chr_1 : list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'O', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#                 -26   -25  -24  -23  -22  -21  -20  -19                                                                                  -2   -1
# default slicing go from left to right 

print(chr_1[0:7]) # 0 : include  | index 7-1 = 6 
print(chr_1[:7])  # not pass any number = all 
print(chr_1[-26:-19]) # -26 : include | index -19-1 = -20
print(chr_1[0:7:1])
print(chr_1[:7:]) 


#                   0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19    20  21   22   23   24   25     
chr_2: list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'O', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#                 -26   -25  -24  -23  -22  -21  -20  -19                                                                                  -2   -1

print(chr_2[::])


#                   0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19    20  21   22   23   24   25     
chr_3 : list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'O', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#                 -26   -25  -24  -23  -22  -21  -20  -19                                                                                  -2   -1

print(chr_3[::2])


#                   0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19    20  21   22   23   24   25     
chr_4 : list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'O', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#                 -26   -25  -24  -23  -22  -21  -20  -19                                                                                  -2   -1

print(chr_4[::-1])

#                     0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18     
chr_5 : list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'O', 'M', 'N', 'P', 'Q', 'R', 'S']
#                   -19   -18  -17  -16  -15  -14  -13  -12  -11  -10  -9   -8   -7   -6   -5   -4   -3   -2   -1

print(chr_5[1:-3])




