#inputs
a=float(input("enter distance km:"))
b=float(input("enter fuel efficiency km per litters:"))
c=float(input("enter fuel price per liter: Rs."))
d=float(input("enter highway charges: Rs."))


#calculations
fuel=a/b
fuelcost=fuel*c
finaltripcost=fuelcost+d


#outputs
print("fuel used is L",fuel)
print("fuel cost is Rs",fuelcost)
print("final trip cost is Rs",finaltripcost)
