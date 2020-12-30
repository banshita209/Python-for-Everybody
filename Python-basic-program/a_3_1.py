a = input("Enter Hours:")
hrs = float(a)
b= input("Enter rate")
rate=float(b)

if hrs>40 :
 pay=hrs*rate
 over_pay=(hrs-40.0)*(rate*0.5)
 total_pay=over_pay+pay
else :
 total_pay=hrs*rate
print(total_pay)