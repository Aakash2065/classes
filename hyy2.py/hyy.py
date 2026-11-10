def calculate_bill(units):
    bll=0
    if units<=100:
        bill=unit*1.50
    elif units<=200:
        bill=100*1.50+(units_100)*2.50
    elifnit<=500:
        bill=(100*1.50)+(100*2.50)+(units-200)*4.00
    else:
        bill=(100*1.50)+(100*2.50)+(300*4.00)+(units-500)*6.00
        return bill
    n=int(input("Enter number of Customers"))
for i in range(1,n+1):
    print (f"\n customer{i}")
    name=input("enter customer name:")
    units=float(input("enter units consumed:" ))
    bill=calculate_bill(units)
    print("customer name:",name)
    print("units :",units)
    print("bill amount:Rs.",round(bill,2))
    