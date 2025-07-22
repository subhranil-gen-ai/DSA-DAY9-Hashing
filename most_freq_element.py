def most_freq_element(arr):
  freq={}
  for i in arr:
    freq[i]=freq.get(i,0)+1
  most_freq_element=max(freq.values())
  for i in arr:
    if freq[i]==most_freq_element:
      return i
arr=[2,4,4,4,3,9]
print(most_freq_element(arr))
