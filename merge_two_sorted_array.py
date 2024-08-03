# write a program to merge two arry in one arry and input arry are sort array
first_array = [3,6,9]
second_array = [2,5,8]
final_array = []
k = 0
l = 0


while(k<len(first_array) and l<len(second_array)):
    if first_array[k]<=second_array[l]:
        final_array.append(first_array[k])
        k = k+1
        #print(k,"k")
    else:
         final_array.append(second_array[l])
         l = l+1
         #print(l)
         #print("no")
while(k<len(first_array)):
    final_array.append(first_array[k])
    k = k+1
while(l<len(second_array)):
    final_array.append(second_array[l])
    l=l+1
print(final_array)

       
