def first_non_repeating_element(arr):
  freq={}
  for i in arr:
    freq[i]=freq.get(i,0)+1
  for i in arr:
    if freq[i]==1:
      return i
arr=[2,2,4,4,1,1,3,9]
print(first_non_repeating_element(arr))
