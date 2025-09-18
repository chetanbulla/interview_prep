
def sum_array_pair(arr,sum):
      arr.sort()
      left=0
      right=len(arr)-1
      while (left<=right):
            if (arr[left]+arr[right]>sum):
                right=right-1
            elif(arr[left]+arr[right]<sum):
                left=left+1
            elif(arr[left]+arr[right]==sum):
                print(arr[left], arr[right])
                right=right+1
                Left=left+1

arr=[5,7,4,3,9,8,19,21]
Sum=17
sum_array_pair(arr,sum)
