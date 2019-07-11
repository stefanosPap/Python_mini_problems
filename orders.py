def get_order(order):
    new_list = [' ']
    menu = ["burger","fries","chicken","pizza","sandwich","onionrings","milkshake","coke"] #menu of the restaurant organised on a list
    initial_len = 1
    for i in range(len(menu)):
        new_order = order.split(menu[i])
        next_len = len(new_order)
        #convert order from string to list
        order = list(order.split(" "))
        #chech if exists
        if (cmp(new_order,order)==1 or cmp(new_order,order)==-1):#cmp works only for Python 2, for Python 3 you can use (new_order > order) - (new_order < order)
            #this for loop is for adding each element nexr_len - initial_len times
            for j in range(next_len-initial_len):
                new_list.extend(menu[i].title())
                new_list.extend(" ")
        #convert new_order from list to string in order to use the split method
        str1 = " "
        new_order=str1.join(new_order)
        order = new_order

    new_list=str1.join(new_list)
    new_list=new_list.replace("   ","#")
    new_list=new_list.replace(" ","")
    new_list=new_list.replace("#"," ")
    print new_list
    return new_list

#Test
get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza")
