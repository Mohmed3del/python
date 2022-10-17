import cmath
import math
def comp(z):
    r=cmath.polar(z)
    print (f"{r[0]}\n{r[1]}")

    # print( math.sqrt(pow(z.real,2)+pow(z.imag,2)))
    # if z.real==0:
    #     print(math.pi/2)
    # else:
    #     print(math.atan2(z.imag, z.real))    
        
    
comp(complex(2+3j))