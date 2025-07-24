def count_unique_element(arr):
  freq={}
  count=0
  for i in arr:
    freq[i]=freq.get(i,0)+1
  for i in arr:
    if freq[i]==1:
      count+=1
  return count
arr=[1,2,4,3,7,6,7,6]
print(count_unique_element(arr))
