incoming =[13, 12, 12, 12, 14, 15, 15, 15, 15, 16, 18, 17, 15, 16, 16, 18, 19, 21, 22, 24, 27, 29, 28, 28, 30, 32, 34, 35, 38, 39, 42, 45, 48, 47, 47, 50, 52, 54, 56, 58, 60, 63, 66, 68, 65, 66, 68, 70, 72, 74, 75, 76, 78, 78, 79]
reference = [0, 4, 9, 14, 18, 23, 28, 32, 37, 42, 47, 51, 56, 61, 65, 70, 75, 80, 84, 89, 94, 98, 103, 108, 113, 117, 122, 127, 131, 136, 141, 146, 150, 155, 160, 164, 169, 174, 178, 183, 188, 193, 197, 202, 207, 211, 216, 221, 226, 230, 235, 240, 244, 249, 254]
print("\n",incoming,"\n")
print("\n",reference,"\n")
def average(indices):
    sum = 0
    avg = 0
    for i in indices:
        sum+=reference[i]
    avg = sum/len(indices)
    return avg
in_array = []
out_array = []
for value in range (256):
    in_array.append(value)
    if value in incoming:
        indices = [i for i, x in enumerate(incoming) if x == value]
        print("corresponding occurances of ",value," are, ",list(reference[i] for i in indices))
        print("average look up value of ", value ,"is, ", average(indices),"\n")
        out_array.append(average(indices))
    else:
        out_array.append(-1)
        
print("input",in_array)
print("output",out_array)
