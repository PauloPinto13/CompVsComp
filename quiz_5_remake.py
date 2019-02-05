def list_sum_function(list_one,list_two):
    for i in range(0,8):
        total_list = list_two[i] + list_one[i]
        print(total_list)
    #total_list = len(list_one + list_two)

##   for i in range(0,len(list_one + list_two)):
##        total_list = list_two[i] + list_one[i]
##        print(total_list)

    return(total_list)


def main():
    
    drinks_tuple = ("soda","coffee","tea","milk")

    for c in range(0,len(drinks_tuple)):
        print(drinks_tuple[c])

    price_tuple = 1.25,2.00,1.75,1.00
    print(sum(price_tuple))

    order_tuple = drinks_tuple + price_tuple

    count = 0

    while (count>(len(order_tuple))):
        count += 1
        print(order_tuple)

    a_list = [3,4,9,14]
    b_list = [5,6,99,3]

    result_list = list_sum_function(a_list,b_list)

    for r in range(0,len(result_list)):
        print(result_list[r])

        
main()
