import numpy as np
def execute(code):
    pathTable = np.array([0,0,0,0,1,0,0,0,0])
    shape = (3,3)
    pathTable = pathTable.reshape(shape)
    orientation = 1
    if code[0] == "L":
            orientation = 2
    elif code[0] == "F":
            orientation = 1
    elif code[0] == "R":
            orientation = 4
    position = [1,1]
    pathTable[position[0],position[1]] = 1
    print 0,orientation,pathTable
    for i in range(0,len(code)):
        #we will find the orientation of the robot to use it for the move 
        
        if code[i] == "L" and orientation == 1:
            orientation = 2
            continue 
        elif code[i] == "L" and orientation == 2:
            orientation = 3
            continue 
        elif code[i] == "L" and orientation == 3:
            orientation = 4
            continue 
        elif code[i] == "L" and orientation == 4:
            orientation = 1
            continue 
         
        if code[i] == "R" and orientation == 1:
            orientation = 4
            continue 
        elif code[i] == "R" and orientation == 2:
            orientation = 1
            continue 
        elif code[i] == "R" and orientation == 3:
            orientation = 2
            continue 
        elif code[i] == "R" and orientation == 4:
            orientation = 3
            continue 
                 
        if code[i] == "F" and orientation == 1:
            orientation = 1
            position[1] += 1  
        elif code[i] == "F" and orientation == 2:
            orientation = 2
        elif code[i] == "F" and orientation == 3:
            orientation = 3
        elif code[i] == "F" and orientation == 4:
            orientation = 4
            position[0] += 1
            
        if orientation == 1:
            d = 1
            a = b = c = 0
        elif orientation == 2:
            a = 1
            b = c = d = 0
        elif orientation == 3:
            c = 1 
            a = b = d = 0
        elif orientation == 4:
            b = 1
            a = c = d = 0
        
        pathTable = np.pad(pathTable,((a,b),(c,d)),'constant',constant_values=0)
        pathTable[position[0],position[1]] = 1
    size = pathTable.shape
    for i in range(size[0]):
        if pathTable[:,i].any() == False:
            pathTable = np.delete(pathTable,i,0)
            size = pathTable.shape
    for i in range(size[1]):
        if pathTable[:,i].any() == False:
            pathTable = np.delete(pathTable,i,1)
    pass
execute("FFFFFLFFFFFLFFFFFLFFFFFL")