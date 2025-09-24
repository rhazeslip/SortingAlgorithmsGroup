#This program implements various sorting algorithms and compares their efficiency based on 
#excution time using various data size sets.


#Bubble Sort Algorithm (Nate Hazeslip)


#Quick Sort Algorithm (Nate Hazeslip)


#Merge Sort Algorithm (Kaden Hyde)
# Recursive function designed to split the inputted array in half until that can no longer be done
# Then merge those two arrays in numerical order
def mergeSort(array, first, last):
    # first = first index of the array
    # last = last index of the array
    if first < last:
        # middle = roughly the middle index of the array, the split point
        middle = (first + (last - 1)) // 2

        # check if the array can be split further, if not, merge, otherwise, split again
        if middle <= first:
            merge(array, first, middle, last)
        else:
            mergeSort(array, first, middle)
            mergeSort(array, middle + 1, last)

# Majority of the sorting happens here, arrays merged in numerical order in this function
def merge(array, first, middle, last):
    # n1 is the length of our "left side" array
    # n2 is the length of our "right side" array
    n1 = middle - first + 1
    n2 = last - middle

    # Temporary arrays to hold the split values until we remerge them
    leftArray = [0] * (n1)
    rightArray = [0] * (n2)

    # Assigning values to temp arrays
    for i in range(n1):
        leftArray[i] = array[first + i]

    for j in range(n2):
        rightArray[j] = array[middle + 1+ j]

    i = 0
    j = 0
    k = first

    # Merge the arrays in numerical order
    while i < n1 and j < n2:
        if leftArray[i] <= rightArray[j]:
            array[k] = leftArray[i]
            i += 1
        else:
            array[k] = rightArray[j]
            j += 1
        k += 1

    # Place in leftover values once the merging is done
    while i < n1:
        array[k] = leftArray[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = rightArray[j]
        j += 1
        k += 1

#Alternate Sorting Algorithm (Seth Wojcik)



#Main Function to test and run algorithms to compare efficiency
def main():
    testArray = [12, 1, 14, 27, 100]
    n = len(testArray)

    print("The given array is:")
    for i in range(n):
        print("%d" % testArray[i], end = " ")
    
    mergeSort(testArray, 0, n - 1)

    print("\n\nThe sorted array is:")
    for i in range(n):
        print("%d" % testArray[i], end = " ")

main()