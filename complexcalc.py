def add(val1,val2):
        real=val1[0]+val2[0]
        complex=val1[1]+val2[1]
        return (real,complex)
def sub(val1,val2):
        real=val1[0]-val2[0]
        complex=val1[1]-val2[1]
        return (real,complex)
def mul(val1,val2):
        real=val1[0]*val2[0]-val1[1]*val2[1]
        complex=val1[0]*val2[1]+val1[1]*val2[0]
        return (real,complex)
def conj(val):return (val[0],-val[1])

def div(val1,val2):
        int=mul(val1,conj(val2))
        real= int[0]/(val2[0]**2+val2[1]**2)
        complex=int[1]/(val2[0]**2+val2[1]**2)
        return (real,complex)
