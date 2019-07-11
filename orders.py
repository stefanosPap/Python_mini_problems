def get_order(order):   
    new_list = [' ']
    menu = ["burger","fries","chicken","pizza","sandwich","onionrings","milkshake","coke"]
    initial_len = 1
    for i in range(len(menu)):
        new_order = order.split(menu[i])
        next_len = len(new_order)
        order = list(order.split(" "))
        if (cmp(new_order,order)==1 or cmp(new_order,order)==-1):
            for j in range(next_len-initial_len):
                new_list.extend(menu[i].title())
                new_list.extend(" ")        
        str1 = " " 
        new_order=str1.join(new_order) 
        order = new_order
        
    new_list=str1.join(new_list)
    new_list=new_list.replace("   ","#")
    new_list=new_list.replace(" ","")
    new_list=new_list.replace("#"," ")    
    print new_list
    return new_list


get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza")
