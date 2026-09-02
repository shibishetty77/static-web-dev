print("hello this is my test.py file")

dict = {}
arr = [3,5,1,2,4,5]
target = 3
for i in arr:
    if (i - target in dict):
        print([dict[i-target],i])
    else:
        dict[i-target] = i