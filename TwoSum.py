# Suppose there is a list [1,4,3,6,7,8,10]
#Which of the two numbers will add upto 10?

def two_sum(list,target):
    dict={}
    for idx, val in enumerate(list):
        compliment= target-list[idx]
        if compliment in dict:
            return idx, dict[compliment]
        else:
            dict[val]=idx

list=[1,4,3,6,7,8,10]
print(two_sum(list,4))
        

print(dict)


