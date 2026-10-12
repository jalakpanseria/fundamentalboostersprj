print("Welcome to the interactive persobnal data collector!!!" , end="\n\n")



name=input("Please enter your name:")
age=int(input("Please enter your age:"))
height_in_meter=float(input("Please enter your heights in meters:"))
fav_num=int(input("Please enter your faviroute number:"))
current_year=int(input("enter current year:"))

print("\n\nThank you! Here is the information we collected")



print("Name:",name,"(Type:",type(name),",Memory Address:",id(name),")")
print("Age:",age,"(Type:",type(age),",Memory Address:",id(age),")")
print("Height:",height_in_meter,"(Type:",type(height_in_meter),",Memory Address:",id(height_in_meter),")")
print("Faviroute number:",fav_num,"(Type:",type(fav_num),",Memory Address:",id(fav_num),")")

print("\n\nYour birth year is approximately:",current_year-age,"(based on your age of" ,age,")")

print("""\n\nThanks for using personal data collector.
      goodbye!!!!""")

