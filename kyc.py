# create a kyc app that collect info from users
# info includes :name,surname,age,gender,state of origin,occupation,tribe

name =input("Enter your first name:") 
lastname =input("enter your surname: ")
age = input("enter your age: ")
gender =input("are you male or female?: ")
state =input("ener your state of origin: ")
occupation =input("what is your occupation?: ")
tribe = input("what nigerian tribeare you from?: ")
print()
#print("customer profile:\t")
print("\tfull name -",name,lastname)
print("\tage -",age)
print("\tgender -",gender)
print("\tstate of origin -",state)
#print("\toccupation -",occupation)
#print("\tTribe-",tribe)
print(f""" customer profile:\t
        -> full name: {name} {lastname}\t
        ->age: {age}\t
        ->gender:{gender}\t
        ->occipation:{occupation}\t
        ->tribe:{tribe}\
""")

        