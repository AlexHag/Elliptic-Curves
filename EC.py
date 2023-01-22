from primes import is_prime
from modsqrt import modsqrt
import secrets

INF_POINT = None

class EC:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p
        self.discriminant = (-16 * (4 * self.a * self.a * self.a + 27 * self.b * self.b)) % self.p
        if self.discriminant == 0:
            raise Exception(f'The parameters a = {self.a}, b = {self.b} form a singularity')
        if(not is_prime(self.p)):
            raise Exception(f'The parameter p = {self.p} is not prime')

    def inverse_mod_p(self, x):
        if x % self.p == 0:
            return None
        return pow(x, self.p - 2, self.p)
    
    def is_on_curve(self, P):
        return (P[1] * P[1]) % self.p == (P[0] * P[0] * P[0] + self.a * P[0] + self.b) % self.p
    
    def get_y_value(self, x):
        n = (x * x * x  + self.a * x + self.b) % self.p
        return modsqrt(n, self.p)
    
    def add_points(self, P, Q):
        if P == INF_POINT:
            return Q
        if Q == INF_POINT:
            return P
        
        if(not self.is_on_curve(P) or not self.is_on_curve(Q)):
            raise Exception(f'The points {P} and {Q} are not on the curve')

        x1 = P[0]
        y1 = P[1]
        x2 = Q[0]
        y2 = Q[1]

        if(x1 % self.p == x2 % self.p and y1 % self.p == -y2 % self.p):
            return INF_POINT
        
        if(x1 % self.p == x2 % self.p and y1 % self.p == y2 % self.p):
            slope = ((3 * x1 * x1 + self.a) * self.inverse_mod_p(2 * y1)) % self.p
        else:
            slope = ((y1 - y2) * self.inverse_mod_p(x1 - x2)) % self.p

        v = (y1 - slope * x1) % self.p

        x3 = (slope * slope - x1 - x2) % self.p
        y3 = (-slope * x3 - v) % self.p

        return (x3, y3)

    def multiply_point(self, k, P):
        Q = INF_POINT
        if k == 0:
            return INF_POINT
        while k != 0:
            if k & 1 != 0:
                Q = self.add_points(Q, P)
            P = self.add_points(P, P)
            k >>= 1
        return Q

# Elliptic Curve Diffie-Hellman Example on SECP256k1
if(__name__ == '__main__'):
    a = 0
    b = 7
    p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
    secp256k1 = EC(a, b, p)
    Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
    Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
    G = (Gx, Gy)

    alice_priv = int(secrets.token_hex(32), 16)
    alice_pub = secp256k1.multiply_point(alice_priv, G)

    bob_priv = int(secrets.token_hex(32), 16)
    bob_pub = secp256k1.multiply_point(bob_priv, G)

    alice_bob_shared = secp256k1.multiply_point(alice_priv, bob_pub)
    bob_alice_shared = secp256k1.multiply_point(bob_priv, alice_pub)
    print(alice_bob_shared == bob_alice_shared)

    print(f"Alice's private key: {hex(alice_priv)}")
    print(f"Alice's public key: ({hex(alice_pub[0])}, {hex(alice_pub[1])})\n")
    print(f"Bob's private key: {hex(bob_priv)}")
    print(f"Bob's public key: ({hex(bob_pub[0])}, {hex(bob_pub[1])})\n")

    print(f"Alice's and bob's shared private key that can be used for symmetric encryption: ({hex(alice_bob_shared[0])}, {hex(alice_bob_shared[1])})")
