def check_subset(arr1,arr2):
  set2=set(arr2)
  for i in arr1:
    if i not in set2:
      return False
  return True
arr1=[1,2,3]
arr2=[1,2,3,4,5]
print(check_subset(arr1,arr2))
