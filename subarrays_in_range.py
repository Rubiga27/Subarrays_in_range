class subarray:
    def sub_array(self,array,b,c):
        arr1=[]
        while(b<=c):
            arr1.append(array[b])
            b+=1
        return arr1
a=list(map(int,input().split()))
b=int(input())
c=int(input())
array1=subarray()
print(*array1.sub_array(a,b,c))