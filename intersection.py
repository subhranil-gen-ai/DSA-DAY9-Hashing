def intersection(arr1,arr2):
  set2=set(arr2)
  intersection=[]
  for i in arr1:
    if i in set2:
      intersection.append(i)
  return intersection
arr1=[1,2,2,7]
arr2=[1,2,3,4,5]
print(intersection(arr1,arr2))
