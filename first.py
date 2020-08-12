n=int(input("Enter number of elements "))
arr=[]
print("Enter elements :")
for i in range(0,n):
    z=int(input())
    arr.append(z)

k=int(input("Enter the value of k:"))
dict={}
for i in range(0,n):
        if((k-arr[i])in dict):
            print(k-arr[i],arr[i])
        else:
            dict[arr[i]]=True
if dict:
    pass
else:   
    print("No matching pair found ")

    
    