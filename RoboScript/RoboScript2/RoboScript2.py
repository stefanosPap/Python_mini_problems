import numpy as np
def execute(code):
    #initializations 
    orientArray = [1,2,3,4]
    pathTable = np.array([0,0,0,0,1,0,0,0,0])   
    shape =(3,3)
    pathTable = pathTable.reshape(shape)
    #initial orientation
    orientation = 1
    position = [1,1]
    pathTable[position[0],position[1]] = 1
    code += " "
    i = 0
    while i < len(code)-1:
        if code[i].isdigit() == False and code[i+1].isdigit() == False:
        #find the orientation of the robot each time to use it for the move 
            if code[i] == "L" and orientation == 1:
                orientation = 2
                i+=1
                continue 
            elif code[i] == "L" and orientation == 2:
                orientation = 3
                i+=1
                continue 
            elif code[i] == "L" and orientation == 3:
                orientation = 4
                i+=1
                continue 
            elif code[i] == "L" and orientation == 4:
                orientation = 1
                i+=1
                continue 
             
            if code[i] == "R" and orientation == 1:
                orientation = 4
                i+=1
                continue 
            elif code[i] == "R" and orientation == 2:
                orientation = 1
                i+=1
                continue 
            elif code[i] == "R" and orientation == 3:
                orientation = 2
                i+=1
                continue 
            elif code[i] == "R" and orientation == 4:
                orientation = 3
                i+=1                
                continue 
            
            #change positions only for cases 1 and 4, in cases 2 and 3 positions are changed automatically from padding
            if code[i] == "F" and orientation == 1:
                position[1] += 1  
            elif code[i] == "F" and orientation == 4:
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
            i+=1
        #case of digits 
        else:
            index = orientArray.index(orientation)
            for k in range(i+1,len(code)):
                if code[k].isdigit() == False:     
                    num = k - i - 1 #keep the number of digits 
                    i = k #keep the value of k to change loop's index
                    break
            number = int(code[k-num:k])#keep only the digits and convert it to int 
            #check the character before number 
            if code[k-num-1] == 'R':
                if number%4 == 0:#if divided with 4 it returns in the same orientation 
                    continue
                elif number%4 == 1:
                    if index != 0:
                        orientation = orientArray[index-1]
                    else:
                        orientation = orientArray[3]
                elif number%4 == 2:
                    if index > 1:
                        orientation = orientArray[index]-2                        
                    else:
                        orientation = orientArray[index]+2
                elif number%4 == 3:                    
                    if index != 3:
                        orientation = orientArray[index+1]
                    else:
                        orientation = orientArray[0]
            elif code[k-num-1] == 'L':
                if number%4 == 0:
                    continue
                elif number%4 == 1:
                    if index != 3:
                        orientation = orientArray[index+1]
                    else:
                        orientation = orientArray[0]
                elif number%4 == 2:
                    if index > 1:
                        orientation = orientArray[index]-2                        
                    else:
                        orientation = orientArray[index]+2
                elif number%4 == 3:                    
                    if index != 0:
                        orientation = orientArray[index-1]
                    else:
                        orientation = orientArray[3]
            else:
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
                for p in range(number):
                    if orientation == 1:
                        position[1] += 1
                    elif orientation == 4:
                        position[0] += 1
                    pathTable = np.pad(pathTable,((a,b),(c,d)),'constant',constant_values=0)
                    pathTable[position[0],position[1]] = 1
                   
    #delete useless zeros from the array after loop
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
    #convert to string 
    substring = ''
    for i in range(size[0]):
        for j in range(size[1]):
            if pathTable[i,j] == 1:
                substring += '*'
            else:
                substring += ' '
        if i!=size[0]-1: 
            substring += '\r\n'
    return substring 
execute("")