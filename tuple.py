studentDetails = ("Andre",13,"playing handball")
print(type(studentDetails))

# Packing - The process of assigning values to a tuple is known as packing.
address=(210,"brickfeild apartment","bangalore","karnataka",564000)

for i in address:
    print(i)

# unpacking - unpacking tuples assigns the  objects in a tuple to mulatiple varibles.
houseno,apartment,city,state,pin=address
print("House number:",houseno)
print("apartment name:",apartment)
print("city name:",city)
print("state name:",state)
print("pin number:",pin)

# A tuple can be created without parentheses
mypets="dog","cat","parrot"
print(type(mypets))
print(mypets[0])

myTuple=("mouse",(1,2,3),[10,45,60])
print(myTuple[1][0])

food=("sushi","pasta","indian currys","noodles/ramen","japanese street food")
print(food[1])

# food[1]="fried chicken"
# tuple immutable - you cannot change value of tuple

my_tuple1=("passion fruit","plum")
my_tuple2=("dragon fruit","durian")

my_tuple3=my_tuple1+my_tuple2
print(my_tuple3)

favoritegames=("Minecraft","Roblox","Poppy Playtime","Bendy","Undertale")
print(len(favoritegames))
print(favoritegames*3)