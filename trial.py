def even(num):
    print (num)
    if num % 2 != 0:
        print ("please enter an even number")
    elif num== 2:
        return num
    else:
        return even(num-2)

even(8)