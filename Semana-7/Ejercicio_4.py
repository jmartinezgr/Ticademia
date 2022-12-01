
def lorenz(km):
    km /= 3.6
    s = 1-(km**2)/(299792458**2)   
    return round(1/s**0.5,15)

for i in range(int(input())):
    print(lorenz(float(input())))

