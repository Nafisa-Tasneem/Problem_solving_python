
def taumBday(b, w, bc, wc, z):
    cost = 0
    if (wc == bc):
        cost = b * bc + w * wc
    elif (bc> wc + z) and (z< bc): # here conversion rate, z should be checked carefully.
        #if the total cost after conversion is greater than without conversion, then mininmum cost should be kept

        cost = wc * w + b * (wc + z)
    elif (wc> bc + z) and (z< wc):
        cost = bc * b + w * (bc + z)
    else:
        cost = b * bc + w * wc

    print(cost)
    return cost


t = int(input().strip())

for t_itr in range(t):
    first_multiple_input = input().rstrip().split()

    b = int(first_multiple_input[0])

    w = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    bc = int(second_multiple_input[0])

    wc = int(second_multiple_input[1])

    z = int(second_multiple_input[2])

    result = taumBday(b, w, bc, wc, z)