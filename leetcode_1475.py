#1475. Final Prices With a Special Discount in a Shop

def finalPrices(self, prices: List[int]) -> List[int]:
    for i in range(len(prices)):
        for j in range(len(prices)):
            if j > i and prices[j] <= prices[i]:
                prices[i] = prices[i] - prices[j]
                break
    return prices