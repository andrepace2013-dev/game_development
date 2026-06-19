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
    if choice==4:
        cfc=input('Enter a country')
        print(c_c[cfc])
    if choice==5:
        cd=input('what country do you want to delete')
        del c_c[cd]
        print('Sucsessfully Deleted')
    if choice==6:
        break
