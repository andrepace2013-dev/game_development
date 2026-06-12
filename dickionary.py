c_c={}
while True:
    print("1. Insert")
    print("2. Display all countries")
    print("3. Display all capitals")
    print("4. Get capital")
    print("5. Delete")
    print("6. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        country=input('Enter a country')
        capital=input('Enter the capital')
        c_c[country]=capital
    if choice==2:
        print(c_c.keys())
    if choice==3:
        print(c_c.values())