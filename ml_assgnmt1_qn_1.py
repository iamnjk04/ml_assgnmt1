from typing import List
list_a = [1,2,3,4,5,6]
list_b = [10,20,30,40,50,60]

def odd_index_comprehension(list_a:List, list_b:List)->List:
    [list_a.append(list_b[i+1]) for i in range(0,len(list_b),2)]
    return list_a

list_a = odd_index_comprehension(list_a,list_b)
print("The resultant output is:")
print(list_a)

