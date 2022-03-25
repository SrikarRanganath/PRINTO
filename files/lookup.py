image1 = [1,12,12,1,2,3,4,1,2,4]
image2 = [11,23,12,21,43,12,3,2,43,34]
print("\n",image1,"\n")
print("\n",image2,"\n")
def average(indices):
    sum = 0
    avg = 0
    for i in indices:
        sum+=image2[i]
    avg = sum/len(indices)
    return avg

for value in range (256):
    if value in image1:
        indices = [i for i, x in enumerate(image1) if x == value]
        print("occurances of ",value," are, ",indices)
        print("average look up value of ", value ,"is, ", average(indices),"\n")
        
