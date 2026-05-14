array=list(map(int,input("Enter the array :").split(",")))
target=int(input("Enter the target : "))
list1=[]
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]+array[j]==target:
            list1.append([array[i], array[j]])
print(list1)