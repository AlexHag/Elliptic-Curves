# Euler's Criterion
def is_qudratic_residue(n, p):
    # The trivial case
    if(n % p == 0):
        return True
    return pow(n, (p - 1) // 2, p) == 1

# The tonelli-shanks algorithm
def modsqrt(n, p):
    # Trivial case
    if(n % p == 0):
        # print(f"n % p == 0 {n} is a trivial quadratic residue 0.")
        return 0
    
    if not is_qudratic_residue(n, p):
        # print(f"n = {n} is not a quadratic residue.")
        return None
    
    # Case p = 3 mod 4
    if(p % 4 == 3):
        # print(f"n = {n} is a quadratic residue.")
        return pow(n, (p + 1) // 4, p)
    
    # Now p = 1 mod 4
    # Step one: find Q and S such that p - 1 = Q(2^S) 
    Q = p - 1
    S = 0
    while(Q % 2 == 0):
        S += 1
        Q //= 2
    # print("Q = ", Q)
    # print("S = ", S)

    # Step two: find a non quadratic residue z
    z = 2
    while is_qudratic_residue(z, p):
        z += 1
    # print(z)

    # Step three: Initialize M, c, t, R
    M = S
    c = pow(z, Q, p)
    t = pow(n, Q, p)
    R = pow(n, (Q + 1) // 2, p)
    # print(f"M = {M}\tc = {c}\tt = {t}\tR = {R}")


    while(t != 1):
        # Calculate the least i, 0 < i < M such that t^2^i = 1
        i = 0
        temp = t
        while temp != 1:
            i += 1
            temp = (temp * temp) % p
        
        # Calculate b, M, c, t, R
        b = pow(c, pow(2, M - i - 1), p)
        M = i
        c = (b * b) % p
        t = (t * b * b) % p
        R = (R * b) % p
        # print(f"b = {b}\tM = {M}\tc = {c}\tt = {t}\tR = {R}")

    # We have found the square root R
    return R
