def large_cont_sum(arr):
    max_sum = arr[0]
    for i in arr[1:]:
        max_sum = max(max_sum, max_sum + i, i)
    return max_sum


print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))
