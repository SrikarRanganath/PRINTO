reference = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 9.0, 0.0, 18.0, 35.2, 56.0, 51.0, 58.5, 75.0, -1, 80.0, 84.0, -1, 89.0, -1, -1, 94.0, 105.5, 98.0, 113.0, -1, 117.0, -1, 122.0, 127.0, -1, -1, 131.0, 136.0, -1, -1, 141.0, -1, -1, 146.0, -1, 157.5, 150.0, -1, 164.0, -1, 169.0, -1, 174.0, -1, 178.0, -1, 183.0, -1, 188.0, -1, -1, 193.0, -1, 207.0, 204.0, -1, 209.0, -1, 221.0, -1, 226.0, -1, 230.0, 235.0, 240.0, -1, 246.5, 254.0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
incoming = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255]
print(incoming,"\n")
print(reference,"\n")

"""
for i in range(256):
    if i in incoming:
        index = incoming.index(i)
        continue
    else:
        incoming.insert(index+1,i)
        reference.insert(index+1,-1)
        index+=1

print(incoming,"\n")
print(reference,"\n")
"""

start_index = 0
end_index = 0
current_index  = 0

def approximate(start_index , end_index):
    if end_index < 256 and start_index!=-300:
        n1 = reference[start_index]
        n2 = reference[end_index] 
        d1 = incoming[start_index]
        d2 = incoming[end_index] 
        step_size = (n2 - n1) / (d2 - d1)
        for i in range (start_index+1 , end_index):
            reference[i]=(reference[i-1] + step_size)
    elif end_index >= 256 and start_index!=-300:
        for i in range (start_index+1 , 256):
            reference[i]=255
    elif end_index <256 and start_index==-300:
        for i in range(0,end_index):
            reference[i]=reference[end_index]



i = 0
while( i < 255):
    if reference[i] == -1:
        start_index = i - 1
        end_index = i
        while(reference[end_index] == -1):
            end_index+=1        
            if end_index > 255:
                end_index = 300
                break
        i = end_index;
        if start_index < 0:
            start_index = -300
        #print("\n",start_index)
        #print("\n",end_index,"\n")
        approximate(start_index,end_index)
    i+=1
for i in range(256):
    reference[i] = round(reference[i])
print("\n",reference,"\n")




