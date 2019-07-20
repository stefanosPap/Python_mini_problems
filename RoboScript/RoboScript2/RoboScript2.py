import numpy as np
def execute(code): 
    pathTable = np.array([0,0,0,0,1,0,0,0,0])   
    shape =(3,3)
    pathTable = pathTable.reshape(shape)
    #initial orientation
    orientation = 1
    position = [1,1]
    pathTable[position[0],position[1]] = 1
    execution(code,orientation,pathTable,position)

    #delete useless zeros from the array 
    size = list(pathTable.shape)
    i = 0 
    while i < size[0]:
        if pathTable[i,:].any() == False:
            pathTable = np.delete(pathTable,i,0)
            size = list(pathTable.shape)
            i = 0
            continue
        i+=1
    i = 0
    while i < size[1]:
        if pathTable[:,i].any() == False:
            pathTable = np.delete(pathTable,i,1)
            size = list(pathTable.shape)
            i = 0
            continue
        i+=1
    size = list(pathTable.shape)
    substring = ''
    for i in range(size[0]):
        for j in range(size[1]):
            if pathTable[i,j] == 1:
                substring += "*"
            else:
                substring += " "
        substring += "\r\n"
    print substring
def execution(code,orientation,pathTable,position):
    for i in range(0,len(code)):
        #we will find the orientation of the robot each time to use it for the move 
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
        
        if code[i].isdigit() == True:
            for k in range(int(code[i])):
                execution("F",orientation,pathTable,position)
        """
            position[1] += int(code[i]) - 1   
            dValue = int(code[i]) - 1 
        elif code[i].isdigit() == True and orientation == 2:
            orientation = 2
           #position[0] -= (int(code[i])-2)
            aValue = int(code[i]) - 1 
        elif code[i].isdigit() == True and orientation == 3:
            orientation = 3
            #position[1] -= (int(code[i])-2)
            cValue = int(code[i]) - 2 
        elif code[i].isdigit() == True and orientation == 4:
            orientation = 4
            position[0] += int(code[i]) - 1 
            bValue = int(code[i]) - 1 
        """
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
    return pathTable
execute("LF2RF3RF3RF7")