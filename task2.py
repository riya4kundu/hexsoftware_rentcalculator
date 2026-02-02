total_rent = int(input("enter the total rent="))
food = int(input("enter the food charges="))
water_rent = int(input("enter the water charges="))
elec_rent = int(input("enter the electric charges="))
person = int(input("enter the number of tenants="))
total_amount= (total_rent + food + water_rent + elec_rent)/person
print("each person will pay=", total_amount)
