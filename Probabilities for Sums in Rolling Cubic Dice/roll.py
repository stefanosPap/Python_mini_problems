from itertools import product
def rolldice_sum_prob(sum_, dice_amount):
    if dice_amount * 6 < sum_:  
        return 0
    else:
        per = list(i for i in product([1,2,3,4,5,6],repeat = dice_amount) if sum(i) == sum_)
        result = len(per) / (6**dice_amount)
        return result 


print(rolldice_sum_prob(8, 2))            