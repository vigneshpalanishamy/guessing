import random

print("costa rica")
print("Japan")
print("switzerland")
print("maldives")
print("new zealand")
print("mangolia")
print("venezuela")
print("dubai")
print("france")
print("norway")
print("greece")
 

a = ['costa rice', 'japan', 'switzerland', 'maldives', 'new zealand', 'mangolia', 'venezuela', 'dubai', 'france', 'norway', 'greece']

for _ in range(3):
   user_input = input("Try your Luck:")
   country =random.choice(a)
   print(country)

   if user_input == country:
    print("You are really lucky")
   else:
     print("Don't give up")
 
print("you are lost")
