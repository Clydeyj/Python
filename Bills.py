
def billdiv (bill,  npeeps):
    amtShared = (bill / npeeps)
    tip= amtShared * 0.10
    total = tip + amtShared
    print("Your total bill is ", bill)
    print("The amout you pay is ",total)

billdiv(100, 10)

billdiv(100, 10)
