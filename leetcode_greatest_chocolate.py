
candies = [2, 3, 5, 1, 3]
extraCandies = 3

def kidsWithCandies(candies, extraCandies) :
    maxi = 0
    for i in candies:
        if i >= maxi:
            maxi = i

    output = []

    for i in candies:
        ans = False
        if i + extraCandies >= maxi:
            ans = True
        # else:
        #     ans = 'false'
        output.append(ans)
    # print(output)
    return output


x = kidsWithCandies(candies, extraCandies)