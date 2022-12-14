n = int(input())
counter = 0  # coins
i_counter = 0
answer = True
boardMatrix = []
for i in range(n):
    boardMatrix.append(list(input()))


pX, pY = input().split()  # pacman
pX, pY = int(pX)-1, int(pY)-1
sequenceLength = int(input())
movement = input()



numberOfGhosts = int(input())
gXarray = []
gYarray = []
gMoveArray = []
for ghost in range(numberOfGhosts):
    gX, gY = input().split()  # GhostbI
    gX, gY = int(gX)-1, int(gY)-1
    gXarray.append(gX)
    gYarray.append(gY)
    GhostSequenceLength = int(input())
    gMoveArray.append(input())



#boardMatrix[pX][pY] = "E"
massivPacman = []
massivPacman.append([pX, pY])

for direction in movement:
    if direction == "U":
        pX -= 1
        massivPacman.append([pX, pY])
        #print(boardMatrix[pX][pY])
        if boardMatrix[pX][pY] == "C":
            counter += 1
            boardMatrix[pX][pY] = " "
        elif boardMatrix[pX][pY] == "W":
            answer = False
        #boardMatrix[pX][pY] = "E"

    elif direction == "D":
        pX += 1
        massivPacman.append([pX, pY])
        #print(boardMatrix[pX][pY])
        if boardMatrix[pX][pY] == "C":
            counter += 1
            boardMatrix[pX][pY] = " "
        elif boardMatrix[pX][pY] == "W":
            answer = False
        #boardMatrix[pX][pY] = "E"
        #print(pX, pY)
    elif direction == "L":
        pY -= 1
        massivPacman.append([pX, pY])
        #print(boardMatrix[pX][pY])
        if boardMatrix[pX][pY] == "C":
            counter += 1
            boardMatrix[pX][pY] = " "
        elif boardMatrix[pX][pY] == "W":
            answer = False
            #print(pX, pY)
        #boardMatrix[pX][pY] = "E"
        #print(pX, pY)
    elif direction == "R":
        pY += 1
        massivPacman.append([pX, pY])
        #print(boardMatrix[pX][pY])
        if boardMatrix[pX][pY] == "C":
            counter += 1
            boardMatrix[pX][pY] = " "
        elif boardMatrix[pX][pY] == "W":
            answer = False
        #boardMatrix[pX][pY] = "E"
        #print(pX, pY)
    i_counter += 1

ghost_counter = 0
monster_movement_coordinates = []
general_all_monsters_combined_array = []
for gX_start, gY_start, gMovement in zip(gXarray, gYarray, gMoveArray):
    monster_movement_coordinates = [[gX_start, gY_start]]
    for gMovement_direction in gMovement:

        if gMovement_direction == "U":
            gX_start -= 1
            ghost_counter += 1
            if ghost_counter == 1:
                boardMatrix[gX_start][gY_start] = "C"

        elif gMovement_direction == "D":
            gX_start += 1
            ghost_counter += 1
            if ghost_counter == 1:
                boardMatrix[gX_start][gY_start] = "C"

        elif gMovement_direction == "L":
            gY_start -= 1
            ghost_counter += 1
            if ghost_counter == 1:
                boardMatrix[gX_start][gY_start] = "C"

        elif gMovement_direction == "R":
            gY_start += 1
            ghost_counter += 1
            if ghost_counter == 1:
                boardMatrix[gX_start][gY_start] = "C"

        monster_movement_coordinates.append([gX_start, gY_start])

    general_all_monsters_combined_array.append(monster_movement_coordinates)

#print(general_all_monsters_combined_array)
#print(line)
#k += line.count("C")
#k += line
#print(boardMatrix)
#print(massivPacman)
#print(pX, pY)
#print(sequenceLength, movement)
#print(140, 125, 660, 653, 762)
#print(5, 16, 40, 26, 129)
if answer is True:
    i_counter = 0
    for pacman_path in massivPacman:
        for monsters_path in general_all_monsters_combined_array:
            print(i_counter)
            print(monsters_path)

            if monsters_path[i_counter][0] == pacman_path[0] and monsters_path[i_counter][1] == pacman_path[1]:
                answer = False
                break
        if answer is False:
            break
        i_counter += 1

counter_pidor = 0
if answer is True:
    print(counter, "YES")
else:
    for direction in movement:
        print("i_counter: ", i_counter)
        print("counter_pidor: ", counter_pidor)
        if counter_pidor == i_counter:
            print(counter, "NO")
            exit()
        else:
            if direction == "U":
                pX -= 1
                massivPacman.append([pX, pY])
                # print(boardMatrix[pX][pY])
                if boardMatrix[pX][pY] == "C":
                    counter += 1
                    # print(pX, pY)
                boardMatrix[pX][pY] = "E"

            elif direction == "D":
                pX += 1
                massivPacman.append([pX, pY])
                # print(boardMatrix[pX][pY])
                if boardMatrix[pX][pY] == "C":
                    counter += 1
                    # print(pX, pY)
                boardMatrix[pX][pY] = "E"
                # print(pX, pY)
            elif direction == "L":
                pY -= 1
                massivPacman.append([pX, pY])
                # print(boardMatrix[pX][pY])
                if boardMatrix[pX][pY] == "C":
                    counter += 1
                    # print(pX, pY)
                boardMatrix[pX][pY] = "E"
                # print(pX, pY)
            elif direction == "R":
                pY += 1
                massivPacman.append([pX, pY])
                # print(boardMatrix[pX][pY])
                if boardMatrix[pX][pY] == "C":
                    counter += 1
                    # print(pX, pY)
                boardMatrix[pX][pY] = "E"
        counter_pidor += 1