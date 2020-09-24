def computepay(h,r):
    if h>40:
         return 40*r+(h-40)*1.5*r
    else:
        return 40*h
   

h = int(input("Enter Hours:"))
r= float(input("enter the rate:"))
p = computepay(h,r)
print("Pay",p)
