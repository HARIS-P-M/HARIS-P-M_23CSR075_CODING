array=list(map(int,input("Enter the array elements: ").split(","))) #getting the array input
length=len(array) #finding the length of the array
i=0
max1=array[0] #initializing the max1 with the first element of the array
max2=array[i+1] #initializing the max2 with the second element of the array
while i<length-1:
    if array[i]>max1: #if the current element is greater than max1 then update max1 and max2
        max2=max1
        max1=array[i]
    elif array[i]>max2 and array[i]!=max1: #if the current element is greater than max2 and not equal to max1 then update max2
        max2=array[i]
    i+=1
if(max2==max1): #if max2 is equal to max1 then it means there is no second distinct element in the array
    print("-1 (no second distinct element.)")
else:
    print("The second largest element is: ",max2)