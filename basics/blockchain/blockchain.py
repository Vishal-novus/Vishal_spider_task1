
import random, math
from time import time
from fractions import Fraction

random.seed(time())

class Poly():
    def __init__(self, coeffs: list[int]|tuple[int], degree: int) -> None:
        assert len(coeffs) == degree + 1, "The number of coefficients does not match with the given degree"
        self.coeffs = coeffs
        self.degree = degree
    
    def coeff(self, power: int) -> int:
        return self.coeffs[power]
    
    def value(self, x: int) -> int:
        ret: int = 0
        for i in range(self.degree + 1):
            ret += self.coeff(i) * int(math.pow(x,i))
        return ret
    
def SSSencrypt(S: int, N: int, K: int) -> list[tuple[int]]:
    ret: list[tuple[int]] = list()

    coeffs: list[int] = [S]
    for _ in range(K-1):
        coeff: int = 0
        while not coeff: coeff = random.randrange(1000) #arbitary choice of 1000
        coeffs.append(coeff)
    poly: Poly = Poly(coeffs, K-1)

    for i in range(1,N+1): 
        ret.append((i, poly.value(i)))
    
    return ret

def SSSdecrypt(points: list[tuple[int]]) -> int:
    L: list[int] = list()
    K: int = len(points)

    for i in range(K):
        p: Fraction = Fraction(1,1)
        for j in range(K):
            if j == i : continue
            p *= Fraction( -points[j][0], points[i][0] - points[j][0] )
        L.append(p)

    S: int = 0
    for i in range(K):
        S += L[i] * points[i][1]

    return S

if __name__ == "__main__":
    S: int = 67
    N: int = 7
    K: int = 5

    points = SSSencrypt(S,N,K)
    print("The points generated are")
    for point in points:
        print(point)
    secret: int = SSSdecrypt(points[:K])
    print(f"We can use any {K} (or more) points to reconstruct the secret")
    print(f"The secret is {secret}")