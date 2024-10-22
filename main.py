# Put your function here
def decreaseElements(vals):
    for i in range(len(vals)):
        for j in range(len(vals[i])):
             vals[i][j] -= 1
    return vals
# testing
nums = [[96,5,23,16,45,63],[20,106,50,27,38,15]]
print(decreaseElements(nums))
