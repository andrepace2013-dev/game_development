videogames=["Minecraft","Roblox","Poppy Playtime","Garthen of Banban","Microsoft flight simulator 2024","Bendy and the ink machine","Little nightmares","Project Playtime","Meccha Chameleon","Portal","Portal 2","Undertale"]
print(videogames[7])
videogames.append("Deltarune")
print(videogames)
videogames.insert(2,"Subnuatica 2")
print(videogames)
print(len(videogames))
videogames.pop()
print(videogames)
videogames.pop(5)
print(videogames)
#2dlist
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[1][1])
print("Number of rows :",len(matrix))
print("Number of collum :",len(matrix[0]))
for i in range (3):
    for j in range (3):
        print(matrix[i][j],end=" ")
    print("\n")