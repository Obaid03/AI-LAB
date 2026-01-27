N =int(input("Enter A Number: "))
counter=0
for i in range(1,N+1,1):
  if i % 2 ==0:
    counter +=1
    print(i)
print("Total Even Numbers: ", counter)
