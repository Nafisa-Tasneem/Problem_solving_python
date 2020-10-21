heights = [1,2,3,4,5]
sorted_h = sorted(heights)
cnt = 0
for i in range(len(heights)):
    if sorted_h[i] != heights[i]:
        cnt +=1
print(cnt)