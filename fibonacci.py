getallen = int(input('hoeveel termen? '))
n1, n2 =0, 1
count = 0
if getallen <= 0:
   print("Please enter a positive getal ")
elif getallen == 1:
   print("Fibonacci sequence upto",getallen,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < getallen:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1