def word_frequency_counter(string):
    string=string.lower() #convert into lower case
    frequency={}
    #count the frequency of each word in the string
    for word in string.split():
        if word in frequency:
            frequency[word]+=1 #if the word is already in the frequency dictionary increment the count by 1
        else:
            frequency[word]=1 #if the word is not in the frequency dictionary add the count as 1
    return frequency #return the frequency dictionary

string=input("Enter a string: ") #getting the input
frequency=word_frequency_counter(string) #calling the function
print(max(frequency, key=frequency.get)) #finding the word with the highest frequency and printing it
