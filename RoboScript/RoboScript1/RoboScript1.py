def highlight(code):
    colors = {'F': "pink",'L':"red",'R':"green","0":"orange","1":"orange","2":"orange","3":"orange","4":"orange","5":"orange","6":"orange","7":"orange","8":"orange","9":"orange"}
    length = len(code)
    code += " " # add a space at the end in order to avoid limit exceed 
    highlighted = ""
    i=0
    while i<length:
            if code[i] == code[i+1] and code[i].isdigit() == False and code[i] != '(' and code[i] != ')':
                count = 1
                for j in range(i,len(code)):
                    if code[j] == code[j+1]:
                        count +=1
                    else:
                        highlighted += '<span style="color: ' + colors[code[i]] + '">' + code[i]*count + '</span>'
                        i = j
                        break
            elif (code[i].isdigit() == True and code[i+1].isdigit() == True):#case of digit 
                substring = code[i]
                for j in range(i,len(code)):
                    if (code[j].isdigit() == True and code[j+1].isdigit() == True):
                        substring += code[j+1]
                    else:
                        highlighted += '<span style="color: ' + colors[code[i]] + '">' + substring + '</span>'
                        i = j #skip the consecutive digits after colorize them 
                        break
            else:
                if code[i] == '(' or code[i] == ')': #case of ( or )
                    highlighted += code[i]
                    i+=1
                    continue
                if code[i] != " ":#because there is a space at the end of the code 
                    highlighted += '<span style="color: ' + colors[code[i]] + '">' + code[i] + '</span>'
            i+=1
    return highlighted
print highlight("22L7LF551FL391L392F7(")
