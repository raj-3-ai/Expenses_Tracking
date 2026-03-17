def Moving_zeros(arr):
   result=[]
   for i in arr:
    if i!=0:
        result.append(i)
   zeros=len(arr)-len(result)
   for i in range(zeros):
        result.append(0)  
   return(result)    
arr = [12, 5, 0, 18, 7, 0, 3, 25, 10]
print(Moving_zeros(arr))