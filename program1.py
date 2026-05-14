array=list(map(int,input("Enter the array elements: ").split(",")))
length=len(array)
i=0
max1=array[0]
max2=array[i+1]
while i<length-1:
    if array[i]>max1:
        max2=max1
        max1=array[i]
    elif array[i]>max2 and array[i]!=max1:
        max2=array[i]
    i+=1
if(max2==max1):
    print("-1 (no second distinct element.)")
else:
    print("The second largest element is: ",max2)