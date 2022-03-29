import numpy as np

# image 1 is reference 
# image 2 is incoming 

reference = [249, 248, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 245, 113, 218, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255] 

 

incoming = [251, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 253, 252, 254, 253, 252, 253, 253, 255, 253, 254, 254, 255, 253, 253, 254, 252, 253, 252, 253, 252, 253, 251, 253, 251, 253, 254, 253, 252, 254, 253, 253, 254, 254, 254, 254, 253, 252, 253, 253, 252, 249, 253, 252, 251, 252, 251, 254, 252, 253, 253, 252, 253, 253, 252, 253, 253, 253, 253, 252, 252, 252, 252, 252, 253, 253, 253, 253, 253, 253, 253, 252, 252, 252, 252, 252, 251, 252, 253, 253, 252, 251, 252, 252, 252, 252, 252, 252, 252, 252, 252, 253, 252, 252, 252, 252, 252, 252, 253, 253, 252, 252, 253, 254, 254, 254, 254, 255, 254, 253, 254, 254, 254, 254, 254, 254, 254, 254, 255, 254, 254, 254, 254, 254, 254, 254, 254, 254, 253, 254, 253, 254, 254, 254, 254, 254, 254, 254, 254, 253, 254, 254, 254, 254, 254, 253, 254, 254, 254, 253, 254, 253, 254, 254, 254, 254, 254, 253, 254, 254, 254, 254, 254, 254, 253, 250, 251, 252, 253, 253, 253, 254, 254, 253, 254, 253, 253, 254, 254, 253, 253, 254, 252, 252, 252, 253, 253, 253, 253, 253, 254, 254, 254, 254, 253, 254, 254, 254, 254, 254, 254, 254, 253, 253, 253, 253, 253, 253, 253, 253, 254, 253, 253, 254, 254, 253, 253, 253, 253, 254, 254, 252, 253, 254, 254, 253, 253, 254, 254, 253, 253, 253, 253, 252, 254, 252, 253, 253, 253, 252, 253, 253, 253, 253, 253, 253, 252, 252, 253, 253, 253, 253, 252, 253, 253, 254, 253, 252, 253, 253, 252, 253, 253, 252, 253, 253, 253, 252, 253, 253, 253, 253, 253, 253, 253, 253, 252, 252, 253, 253, 252, 253, 253, 252, 253, 253, 253, 253, 253, 253, 252, 252, 252, 253, 253, 253, 253, 253, 251, 253, 252, 253, 252, 253, 252, 252, 252, 252, 252, 252, 253, 252, 252, 251, 252, 253, 252, 251, 252, 252, 254, 252, 252, 252, 252, 252, 252, 252, 252, 252, 253, 252, 251, 252, 251, 251, 251, 251, 247, 252, 251, 251, 251, 251, 251, 249, 250, 251, 250, 252, 253, 253, 251, 254, 251, 252, 252, 250, 253, 251, 252, 251, 250, 251, 253, 253, 251, 252, 248, 251, 250, 250, 253, 250, 250, 250, 251, 251, 250, 250, 251, 251, 250, 248, 249, 248, 249, 247, 247, 251, 252, 250, 248, 248, 250, 250, 250, 249, 251, 247, 248, 250, 250, 248, 251, 247, 250, 247, 250, 251, 249, 251, 250, 246, 247, 246, 250, 251, 250, 251, 246, 245, 251, 250, 249, 248, 248, 251, 249, 249, 248, 248, 248, 245, 252, 247, 246, 245, 247, 251, 250, 251, 248, 251, 246, 247, 249, 250, 250, 248, 250, 249, 249, 248, 249, 249, 250, 249, 247, 249, 248, 247, 250, 251, 250, 246, 247, 247, 251, 250, 248, 250, 252, 249, 249, 250, 252, 248, 246, 251, 249, 249, 250, 248, 249, 247, 247, 251, 248, 248, 248, 243, 251, 249, 248, 249, 251, 249, 251, 249, 248, 250, 248, 248, 247, 249, 249, 250, 249, 247, 249, 248, 249, 248, 247, 249, 250, 245, 248, 244, 248, 248, 245, 248, 243, 248, 243, 246, 246, 249, 248, 248, 247, 250, 247, 246, 248, 250, 243, 248, 246, 249, 247, 248, 250, 250, 245, 249, 246, 246, 245, 244, 251, 248, 244, 248, 249, 245, 246, 249, 247, 244, 247, 247, 247, 248, 247, 246, 247, 245, 246, 245, 243, 248, 246, 247, 244, 247, 245, 246, 247, 244, 245, 243, 246, 243, 243, 247, 244, 246, 249, 245, 247, 247, 247, 245, 243, 242, 245, 247, 244, 244, 245, 243, 244, 242, 243, 246, 240, 247, 244, 243, 244, 246, 243, 243, 246, 242, 247, 244, 241, 242, 245, 242, 244, 246, 248, 242, 246, 243, 243, 244, 241, 245, 248, 244, 243, 243, 242, 243, 244, 246, 247, 246, 246, 243, 245, 244, 243, 244, 242, 244, 249, 242, 244, 240, 241, 241, 243, 245, 242, 244, 241, 244, 244, 241, 242, 243, 242, 242, 241, 242, 241, 238, 241, 241, 243, 240, 244, 243, 241, 244, 241, 242, 243, 237, 240, 241, 240, 243, 238, 241, 242, 238, 241, 241, 239, 237, 241, 242, 240, 241, 245, 243, 244, 242, 237, 242, 238, 243, 244, 238, 240, 239, 243, 240, 236, 238, 242, 239, 239, 240, 243, 236, 239, 243, 244, 244, 241, 243, 244, 244, 240, 242, 242, 243, 241, 245, 244, 242, 241, 243, 243, 243, 238, 239, 238, 240, 241, 240, 247, 244, 243, 238, 241, 241, 242, 241, 243, 238, 242, 241, 240, 240, 240, 237, 243, 237, 237, 239, 239, 240, 237, 240, 243, 239, 244, 242, 243, 241, 241, 240, 235, 243, 242, 242, 242, 236, 236, 236, 238, 235, 238, 239, 237, 238, 239, 237, 238, 241, 236, 240, 238, 238, 235, 239, 238, 239, 239, 241, 241, 236, 239, 235, 241, 237, 237, 241, 239, 238, 236, 239, 237, 235, 234, 241, 234, 237, 238, 242, 240, 235, 238, 239, 241, 238, 238, 239, 242, 237, 237, 234, 236, 237, 234, 236, 240, 237, 237, 237, 238, 238, 237, 238, 237, 235, 235, 236, 238, 236, 236, 236, 237, 236, 238, 239, 239, 240, 238, 237, 236, 238, 236, 233, 236, 236, 237, 239, 237, 238, 237, 236, 234, 235, 237, 237, 233, 237, 234, 233, 232, 232, 234, 234, 235, 235, 239, 235, 235, 234, 234, 238, 234, 235, 235, 234, 232, 233, 232, 232, 228, 234, 228, 230, 232, 231, 230, 230, 233, 231, 232, 231, 230, 228, 230, 232, 231, 230, 233, 230, 230, 229, 230, 228, 228, 229, 230, 230, 230, 228, 230, 229, 229, 228, 229, 231, 229, 229, 230, 228, 227, 226, 226, 227, 228, 227, 228, 229, 226, 227, 227, 228, 227, 228, 226, 225, 225, 226, 227, 225, 226, 224, 227, 227, 227, 226, 227, 227, 225, 225, 227, 226, 226, 226, 227, 228, 227, 226, 224, 225, 225, 225, 223, 224, 224, 223, 224, 223, 223, 224, 223, 225, 224, 223, 223, 224, 223, 223, 224, 225, 224] 
print("\nreference = ",reference,"\n")
print("\nincoming = ",incoming,"\n")
def average(indices):
    sum = 0
    avg = 0
    for i in indices:
        sum+=incoming[i]
    avg = sum/len(indices)
    return np.uint8(avg)
lookup_in = []
lookup_out = []
for value in range (256):
    if value in reference:
        indices = [i for i, x in enumerate(reference) if x == value]
        lookup_in.append(value)
        lookup_out.append(average(indices))
        #print("occurances of ",value," are, ",indices)
        #print("average look up value of ", value ,"is, ", average(indices),"\n")
print(lookup_in)        
print(lookup_out)        

