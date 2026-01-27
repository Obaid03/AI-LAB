def sum():
  num1=int(input("Enter Number 1"))
  num2=int(input("Enter Number 2"))
  return num1 + num2
def sub():
  num1=int(input("Enter Number 1"))
  num2=int(input("Enter Number 2"))
  return num1 - num2
while (1):
  print("1: Add Two Numbers\n2: Subtract Two Numbers\n3: exit")
  choice=int(input("Enter Your Choice: "))
  if choice==1:
    Sum=sum()
    print("Result: ",Sum)
  elif choice==2:
    Sub=sub()
    print("Result: ",Sub)
  elif choice==3:
    break
  else:
    print("Wrong Choice")
