def mergeSort(arr):
    if len(arr) > 1:
        #find array midpoint
        mid = len(arr)//2

        #split array into two
        left = arr[:mid]
        right = arr[mid:]

        #recursively call on left half
        mergeSort(left)
        #recursively call on right half
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        #merge array back into original
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        #fill in remaining left elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        #fill in remaining right elements
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
  
  
# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
  
