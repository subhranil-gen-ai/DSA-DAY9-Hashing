def find_common_elements(arr1,arr2):
  common=[]
  set1=set(arr1)
  for num in arr2:
    if num in set1 and num not in common:
      common.append(num)
  return common
arr1=[1,2,3,4,5]
arr2=[3,4,5,6,7]
common=find_common_elements(arr1,arr2)
print(common)
