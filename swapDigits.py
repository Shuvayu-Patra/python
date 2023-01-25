a = []
n = input("Enter the number: ")
for i in n:
    a.append(int(i))
(a[0] , a[len(a)-1]) = ( a[len(a)-1] , a[0])
print(a)
ans=0
l=len(a)
for i in a:
    ans+= i* (10 ** (l-1))
    l-=1
    
print(ans)


