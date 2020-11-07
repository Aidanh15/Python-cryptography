def gcd(a, b):
    #return the greatest Common divisor (GCD) of a and b using euclids algo
    while a != 0:
        a,b = b % a, a
    return b

def findModInverse(a,m):
    # Return modular inverse of a % m which is the no. x such that a * x % m = 1

    if gcd(a, m) !=1:
        return None
       
       
    u1,u2,u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q* v3), v1, v2, v3
    return u1 % m 

#TEST
print(gcd(24, 32)) # should = 8
print(gcd(37, 41)) # shhould = 1
print(findModInverse(7, 26)) #should be 15
print(findModInverse(8953851, 26))
    